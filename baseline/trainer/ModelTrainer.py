import time

import pandas as pd
import torch
import wandb
from accelerate import Accelerator
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, SubsetRandomSampler
from tqdm import trange
from tqdm.auto import tqdm
from transformers import get_scheduler
from config import WANDB_API_KEY


class ModelTrainer:
    def __init__(self, category, model_name):
        self.max_epochs = 50
        self.category = category
        self.model_name = model_name
        self.gpu_available = torch.cuda.is_available()

    def fit(self, model, optimizer, train_dataloader, dev_dataloader, device, accelerator, lr_scheduler):
        """Method for Training loop with Early Stopping based on the DevSet"""
        num_training_steps = self.max_epochs * len(train_dataloader)
        progress_bar = tqdm(range(num_training_steps))

        # EARLY STOPPING CRITERIA
        # Source of the Early Stopping: https://pythonguides.com/pytorch-early-stopping/
        last_loss = 100
        patience = 1
        trigger = 0

        for epoch in trange(self.max_epochs, desc='Epoch'):
            print(f'Started Training Epoch {epoch}')
            # Training
            model.train()
            for step, batch in enumerate(train_dataloader, start=1):
                with accelerator.accumulate(model):
                    batch = {k: v.to(device) for k, v in batch.items()}
                    if self.model_name == 'convbert' or self.model_name == 'electra':
                        outputs = model(input_ids=batch['input_ids'], token_type_ids=batch['token_type_ids'],
                                        attention_mask=batch['attention_mask'], labels=batch['labels'])
                    else:
                        outputs = model(
                            input_ids=batch['input_ids'], attention_mask=batch['attention_mask'], labels=batch['labels'])
                    loss = outputs.loss
                    accelerator.backward(loss)
                    optimizer.step()
                    optimizer.zero_grad()
                    lr_scheduler.step()
                    progress_bar.update(1)
                    wandb.log({"batch": step, "time": time.time()})

            # Evaluation on DevSet
            model.eval()
            loss_lst, dev_predictions, dev_actuals = [], [], []
            for batch in dev_dataloader:
                batch = {k: v.to(device) for k, v in batch.items()}
                with torch.no_grad():
                    if self.model_name == 'convbert' or self.model_name == 'electra':
                        outputs = model(input_ids=batch['input_ids'], token_type_ids=batch['token_type_ids'],
                                        attention_mask=batch['attention_mask'], labels=batch['labels'])
                    else:
                        outputs = model(
                            input_ids=batch['input_ids'], attention_mask=batch['attention_mask'], labels=batch['labels'])
                logits = outputs.logits
                loss = outputs.loss
                loss_lst.append(loss)
                dev_actuals.extend(batch['labels'])
                dev_predictions.extend(torch.argmax(logits, dim=-1))

            current_loss = sum(loss_lst) / len(loss_lst)
            wandb.log({"loss": current_loss, "epoch": epoch})
            dev_predictions = torch.stack(dev_predictions).cpu()
            dev_actuals = torch.stack(dev_actuals).cpu()
            dev_report = classification_report(dev_actuals, dev_predictions, target_names=['non-biased', 'biased'],
                                               output_dict=True)
            wandb.log(
                {"DEV f-1 score": dev_report['weighted avg']['f1-score'], "epoch": epoch})
            print('The current dev loss:', current_loss)
            if current_loss >= last_loss:
                trigger += 1
                print('trigger times:', trigger)

                if trigger >= patience:
                    print('Early stopping!\n Starting evaluation on test set.')
                    break

            else:
                print('trigger: 0')
                trigger = 0
            last_loss = current_loss
        return model

    def evaluate(self, model, test_dataloader, device, fold):
        """Evaluation model on the Test set"""
        num_test_steps = len(test_dataloader)
        progress_bar = tqdm(range(num_test_steps))

        print(f'Start Evaluation')
        predictions, actuals, datasets = [], [], []
        for batch in test_dataloader:
            batch = {k: v.to(device) for k, v in batch.items()}
            with torch.no_grad():
                if self.model_name == 'convbert' or self.model_name == 'electra':
                    outputs = model(input_ids=batch['input_ids'], token_type_ids=batch['token_type_ids'],
                                    attention_mask=batch['attention_mask'], labels=batch['labels'])
                else:
                    outputs = model(
                        input_ids=batch['input_ids'], attention_mask=batch['attention_mask'], labels=batch['labels'])
            logits = outputs.logits
            actuals.extend(batch['labels'])
            predictions.extend(torch.argmax(logits, dim=-1))
            datasets.extend(batch['dataset_id'])
            progress_bar.update(1)

        predictions = torch.stack(predictions).cpu()
        actuals = torch.stack(actuals).cpu()
        datasets = torch.stack(datasets).cpu()
        report = classification_report(actuals, predictions, target_names=[
                                       'non-biased', 'biased'], output_dict=True)
        f1_score = report['weighted avg']['f1-score']
        wandb.log({"TEST f-1 score": f1_score, "fold": fold})
        df_report = pd.DataFrame(report)
        df_report.to_csv(
            f'./Results_new/{self.model_name}-{self.category}-fold-{fold}-report.csv')
        df_predictions = pd.DataFrame(
            data={'predictions': predictions, 'actuals': actuals, 'dataset_id': datasets})
        # Save the predictions for later analysis
        df_predictions.to_csv(
            f'./Results_new/{self.model_name}-{self.category}-fold-{fold}-predictions.csv')
        return f1_score

    def main(self, fold, train_ids, val_ids, data, model, learning_rate, batch_size, gpu_no):
        """Main Method calling the training and evaluation, starting wandb, setting the GPU, and initializes e.g. Optimizer and Accelerator"""
        print(f'Training Initialized for fold {fold}')
        # Initialize Weights & Biases
        wandb.login(key =WANDB_API_KEY, relogin = True)
        wandb.init(project=str(self.category) + str(self.model_name), reinit=True)
        wandb.config = {
            "learning_rate": learning_rate,
            "epochs": 20,
            "batch_size": batch_size,
        }
        wandb.run.name = "Fold-" + str(fold)

        # Set the GPU
        device = torch.device(gpu_no) if self.gpu_available else torch.device("cpu")

        # Create DEV and TEST Set from the K-folds Test Set
        # DEV Set used for early stopping criteria, the test set only for final evaluation
        dev_ids, test_ids = train_test_split(
            val_ids, test_size=0.75, train_size=0.25, random_state=42, shuffle=True)

        train_sampler = SubsetRandomSampler(train_ids)
        dev_sampler = SubsetRandomSampler(dev_ids)
        test_sampler = SubsetRandomSampler(test_ids)

        train_dataloader = DataLoader(
            data, batch_size=batch_size, sampler=train_sampler)
        dev_dataloader = DataLoader(
            data, batch_size=batch_size, sampler=dev_sampler)
        test_dataloader = DataLoader(
            data, batch_size=batch_size, sampler=test_sampler)

        # Push model to GPU
        model.to(device)
        optimizer = torch.optim.AdamW(
            model.parameters(), lr=learning_rate)  # Initialize Optimizer
        # Enable gradient checkpointing to save memory
        model.gradient_checkpointing_enable()
        lr_scheduler = get_scheduler(
            "cosine",
            optimizer=optimizer,
            num_warmup_steps=0,
            num_training_steps=10 * len(train_dataloader)
        )
        # Start Accelerator See https://huggingface.co/docs/transformers/v4.20.1/en/perf_train_gpu_one
        accelerator = Accelerator(
            device_placement=False, cpu=True, gradient_accumulation_steps=4)
        model, optimizer,_,lr_scheduler = accelerator.prepare(
            model, optimizer, train_dataloader, lr_scheduler)

        # Model Training with Dev Evaluation for Early Stopping
        model = self.fit(model, optimizer, train_dataloader,
                         dev_dataloader, device, accelerator, lr_scheduler)

        # Evaluation on TestSet
        score = self.evaluate(model, test_dataloader, device, fold)

        wandb.finish()
        return score
