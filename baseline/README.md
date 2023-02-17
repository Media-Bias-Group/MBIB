# Baseline training & evaluation
Implementation of the experiments performed in the paper. See baseline performance on various tested models below:


| Task | Model | Micro F1 | Macro F1 |
| --- | --- | --- | --- |
| cognitive-bias | ConvBERT/ConvBERT | 0.7126 | 0.7664 |
| fake-news | Bart/RoBERTa-T | 	0.6811 | 0.7533 |
| gender-bias | RoBERTa-T/ELECTRA | 0.8334 | 0.8211 |
| hate-speech | RoBERTA-T/Bart | 0.8897 | 0.7310 |
| linguistic-bias | ConvBERT/Bart | 0.7044 | 0.4995 |
| political-bias | ConvBERT/ConvBERT | 0.7041 | 0.7110 |
| racial-bias | ConvBERT/ELECTRA | 0.8772 | 	0.6170 |
| text-level-bias | ConvBERT/ConvBERT | 0.7697 | 	0.7532 |

## Reproduce results
In order to reproduce the baseline results 
please install the python requirements:
```
pip -r install baseline/requirements.txt
```
and run the training script:
```
python baseline/run_baseline.py
```

## Files descriptions
* `run_baseline.py`
  * script where specifics of the training are defined, see example below
   ```python
    wrapper = TrainerWrapper(5, 'cognitive-bias', "bart", gpu=0,batch_size=64, model_length=78)
    result = wrapper.run()
   ```
* `trainer/model_specifications.py`
    - This file is used by `TrainerWrapper.py` for specification of the model, which is accessed through huggingface.
    - used models:
      * [ConvBert](https://huggingface.co/YituTech/conv-bert-base)
      * [Bart](https://huggingface.co/facebook/bart-base)
      * [TwitterRoBERTa](https://huggingface.co/cardiffnlp/twitter-roberta-base)
      * [GPT2](https://huggingface.co/gpt2)
      * [Electra](https://huggingface.co/google/electra-base-discriminator)
* `trainer/TrainerWrapper.py`
  * This is a wrapper class that wraps tokenization, configuration and training of the model into k-fold cross-validation.
* `trainer/ModelTrainer.py`
  * Main training class using accelerator for improved training and [Weights & Biases](https://wandb.ai/home) for logging. If you want to use the weights & biases, put your wandb API key to the `config.py`