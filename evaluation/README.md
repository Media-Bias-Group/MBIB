# Evaluation on MBIB
The evaluation script allows you to train and evaluate the models on our MBIB benchmark. You can also use the script for evaluation only.

If you want to add your own model for evaluation, add your custom loading function into `model_specification.py`.

For the evaluation run:
```
python evaluation/run_evaluation.py
```
In the `config` in the script you can configure following:
* `number_of_folds`: Number of folds for cross validation, default 5
* `model`: model name key to `model_specification.py` file, where you can either choose from our chosen models or define your own
* `task`: specifies the name of the task from MBIB.
* `eval_only`: if set to True, the training is skipped and model is only evaluated within the CV to ensure the same splits. 
* `batch_size`
* `max_length`
* `max_epoch`




## File descriptions
* `model_specification.py` a file where models and tokenizers are specified. Add your loading function here if you want to use your models.
* `trainer.py` main training class that runs k-fold CV on specified task.
* `run_evaluation.py` script that calls the trainer with specified `config`