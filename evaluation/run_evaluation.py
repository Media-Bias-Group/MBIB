from evaluation.trainer import Trainer


config = {"number_of_folds": 5,
          "model": 'roberta',
          "batch_size": 32,
          "max_length": 128,
          "task": 'cognitive-bias',
          "max_epoch":10,
          "eval_only": False}


trainer = Trainer(**config)
trainer.run()