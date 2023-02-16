# Introducing MBIB - the first Media Bias Benchmark Task and Dataset Collection
![d](figures/transparent.png)

# Introduction
This repository contains all resources from the paper "Introducing MBIB - the first Media Bias Benchmark Task and Dataset Collection". MBIB (Media Bias Identification Benchmark) consists of 22 carefully selected bias datasets.

___

[1. Datasets](#2-datasets)
  * [1. Getting started](#get-started-with-mbib)
  * [2. Dataset processing](#dataset-processing)
  * [3. Create MBIB](#create-mbib)
   
[2. Baseline](#4-baseline)

[3. Citation](#5-citation)

# 1. Datasets
## Get started with MBIB
___
To facilitate research of media bias we share our MBIB corpus on huggingface, to provide an easy entrypoint for data scientists of all skill levels. The corpus can be found on https://huggingface.co/datasets/mediabiasgroup/mbib and fetched through few lines of code:
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
1. `raw` directory contains raw data and `README.md` file with instructions how to obtain the raw data. Few datasets we either cannot distribute or are too large in its raw form, therefore it's on the user to get them according to the instructions.
2. `process.py` is a processing script that generates processed file `id-name.csv` out of raw data.
3. `README.md` contains information about the dataset, citation information and original source.

For one dataset, Twitter API is needed to fetch the data. In order to be able to fetch the tweets, put your twitter API credentials into `config.py`. If you don't have the Twitter API credentials, this dataset will be skipped.

 
## Create MBIB
___
In order, to obtain the full MBIB corpus run
```
python create_corpus.py
```
which processes all the datasets, if the particular raw data are available and subsequently merges the datasets into 8 Tasks. For more information about the Tasks please see our paper.
The output of the script can be found in `/datasets/mbib-full`

The example instances of each MBIB task can be found in the following:

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

| Bias Type |Dataset| Data Points|
|------|-----------|----------|
| Linguistic Bias                                 | Wikipedia NPOV| 11,945               |
|                                                 | BABE                           | 3,673                |
|                                                 | Wiki Neutrality Corpus| 362,991              |
|                                                 | UsVsThem                                | 6,863                |
|                                                 | RedditBias                | 10,583               |
|                                                 | Media Frames Corpus                 | 37,622               |
|                                                 | BASIL                      | 1,726                |
|                                                 | Biased Sentences                                        | 842                  |
|                                                 |                                                                              | Σ 433,677 |
||
| Cognitive Bias                                  | BIGNEWS   | 2,331,552            |
|                                                 | Liar Dataset   | 12,835               |
|                                                 |                                                                              | Σ 2,344,387 |
||
| Text-Level Context | Contextual Abuse Dataset | 26,235|
|                                                 | Multidimensional Dataset     | 2,094                |
|                                                 |                                                                              |Σ 28,329|
||
| Hate Speech                                     | Kaggle Jigsaw         | 1,999,516            |
|                                                 | HateXplain                     | 20,148               |
|                                                 | RedditBias        | 10,583               |
|                                                 | Online Harassment Corpus             | 20,427               |
|                                                 |                                                                              |Σ 2,050,674|
||
| Gender Bias                                     | RedditBias               | 3,000                |
|                                                 | RtGender                         | 15,351               |
|                                                 | WorkPlace sexism                 | 1,136                |
|                                                 | CMSB                   | 13,634               |
|                                                 |                                                                              |Σ 33,121 |
||
| Racial Bias                                     | RedditBias                 | 2,620                |
|                                                 | RacialBias                             | 751                  |
|                                                 |                                                                              |Σ 2,371|
||
| Fake News                                       | Liar Dataset                              | 12,835               |
|                                                 | PHEME                           | 5,222                |
|                                                 | FakeNewsNet                     | 6,337                |
|                                                 |                                                                              |Σ 24,394|
||
| Political Bias                                  | UsVsThem                                  | 6,863                |
|                                                 | BIGNEWS                  | 2,331,552            |
|                                                 | SemEval                             | 9,783                |
|                                                 |                                                                              |Σ 2,348,198|

# 2. Training & Evaluation
In order to reproduce the baseline results from our paper, 
please install the python requirements:
```
pip -r install baseline/requirements.txt
```
and run the training script:
```
python baseline/run_baseline.py
```
For more information about the methods and training procedure please see [README in baseline directory](./baseline/README.md).

# 3. Citation
Please cite us as:
```python
#TODO
```