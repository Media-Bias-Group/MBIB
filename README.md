# Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection
![d](figures/transparent.png)

# Introduction
This repository contains all resources from the paper "Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection". MBIB (Media Bias Identification Benchmark) consists of 22 carefully selected bias datasets.

___

[1. Datasets](#1-datasets)
  * [1. Getting started](#get-started-with-mbib)
  * [2. Dataset processing](#dataset-processing)
  * [3. Create MBIB](#create-mbib)
   
[2. Training & evaluation](#2-training-and-evaluation)

[3. Citation](#5-citation)

# 1. Datasets
## Get started with MBIB
___
To facilitate research of media bias we share our MBIB corpus on huggingface, to provide an easy entrypoint for data scientists of all skill levels. The corpus can be found on https://huggingface.co/datasets/mediabiasgroup/mbib and fetched through a few lines of code:
```python 
from datasets import load_dataset

dataset = load_dataset("mediabiasgroup/mbib", "cognitive-bias")
# use any of the following config names as a second argument:
"cognitive-bias", "fake-news", "gender-bias", "hate-speech", 
"linguistic-bias", "political-bias", "racial-bias", "text-level-bias"
```

## Dataset processing
___
For preprocessing of the datasets, please first install python dependencies:
```
pip install -r datasets/requirements.txt
```
The `/datasets` directory contains directories for all 22 MBIB datasets. We distilled the datasets from broad collection of datasets that we collected. This full collection can be found [here](https://docs.google.com/spreadsheets/d/1BXcDcnBluSzv1bwwAEpRH61ObXd3Mxf66qsOVxilTXM/edit#gid=0).
Each datasets ID is unique within the collection mentioned above.

Each dataset directory is structured as follows:
```
├─ id_name
     |
     ├─── raw
     |    ├─── raw_data
     |    └─── README.md
     |
     ├──── id-name.csv
     ├──── process.py
     └──── README.md
```
Where 
1. `raw` directory contains raw data and `README.md` the file with instructions how to obtain the raw data. Few datasets we either cannot distribute or are too large in their raw form, therefore a user can get them externally according to our instructions.
2. `process.py` is a processing script that generates a processed file `id-name.csv` out of raw data.
3. `README.md` contains information about the dataset, citation information and original source.

For one dataset, the Twitter API is needed to fetch the data. In order to be able to fetch the tweets, put your twitter API credentials into `config.py`. If you don't have the Twitter API credentials, this dataset will be skipped.

 
## Create MBIB
___
In order, to obtain the full MBIB corpus run
```
python create_corpus.py
```
which processes all the datasets, if the particular raw data are available and subsequently merges the datasets into 8 Tasks. For more information about the Tasks please see our paper.
The output of the script can be found in `/datasets/mbib-full`


The final size of each MBIB task as well as sample instance can be seen below. For details about each task and sizes of its datasets please see [README in datasets directory](/datasets/README.md).

| Task | Linguistic Bias |  Cognitive Bias | Text-Level Context | Hate Speech| Gender Bias| Racial Bias| Fake News| Political Bias| 
| -----|--------|-------|-------|-----|-------|-------|-------|------|
| Total size | 433,677 | 2,344,387 | 28,329|2,050,674|33,121 |2,371|24,394|2,348,198|



| Task | Example from the MBIB datasets |
| -|----|
| Linguistic bias | “A Trump-loving white security guard with a racist past shot and killed an unarmed Black man during an unprovoked hotel parking lot attack"|
| Text-level Context Bias |  “The governor [...] observed an influx of Ukrainian citizens who want to stay in Russia until the situation normalises in their country” | 
| Reporting-Level Context Bias | In a presidential campaign, one candidate receives a disproportionate amount of news coverage. | 
| Cognitive Bias | “Republicans are certain that the more people learn the less they’ll like about the Democrats approach” |
| Hate Speech | “I will call my friends and we go [...] up that [...]” |
| Racial bias| “black people have a high crime rate therefore black people are criminals”| 
| Fake news | “Phoenix Arizona is the No 2 kidnapping capital of the world” |
| Gender Bias | “For a woman that is good.” |
| Political bias | “Generally happy with her fiscally prudent, dont-buy-what-you-cant-afford approach [...]” (classified right) vs “[...] some German voters have also begun to question austerity.” (classified left) 



# 2. Training and Evaluation
As a part of our contribution, we share the evaluation script that can be used for evaluating your own models on the MBIB.



**For evaluation on MBIB** please install the python requirements 
```
pip -r install evaluation/requirements.txt
``` 

and run the eval script:
```
python evaluation/run_evaluation.py
```

If you want to evaluate your own models and/or configure the training parameters, please follow instructions in [README in evaluation directory](evaluation/).


Additionally we also share the code of our baseline training for the sake of reproducibility. For more information please see README in [baseline directory](baseline/)


# 3. Citation
Please cite us as:
```python
@inproceedings{
    title = {Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection},
    author = {Wessel, Martin and Horych, Tomáš and Ruas, Terry and Aizawa, Akiko and Gipp, Bela and Spinde, Timo},
    year = {2023},
    note = {[in review]}
}
```
