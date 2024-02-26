# Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection
![d](figures/transparent.png)

# Introduction
This repository contains all resources from the paper "Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection". MBIB (Media Bias Identification Benchmark) consists of 22 carefully selected bias datasets.
The paper can be found on https://media-bias-research.org/wp-content/uploads/2023/04/Wessel2023Preprint.pdf

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
To facilitate research of media bias we share our MBIB corpus on huggingface, to provide an easy entrypoint for data scientists of all skill levels. The corpus can be found on https://huggingface.co/datasets/mediabiasgroup/mbib-base and fetched through a few lines of code:
```python 
from datasets import load_dataset

dataset_dict = load_dataset("mediabiasgroup/mbib-base")
gender_dataset = dataset_dict['gender_bias']

# use any of the following config names as a second argument:
"cognitive_bias", "fake_news", "gender_bias", "hate_speech", 
"linguistic_bias", "political_bias", "racial_bias", "text_level_bias"
```
### Note
___
Due to the fact that not all MBIB tasks are available for public distribution, we share our benchmark dataset in two versions
- `mbib-base` which consists only from publicly available datasets
- `mbib-full` which can be generated by following instructions later in this document  


## Install dependencies
___
In order to be able to run scripts for data processing, baseline and your own evaluation, please first install python dependencies via following:

```
pip install -r datasets/requirements.txt
```

## Dataset processing
___

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



**For evaluation on MBIB** run the eval script:
```
python evaluation/run_evaluation.py
```

If you want to evaluate your own models and/or configure the training parameters, please follow instructions in [README in evaluation directory](evaluation/).


Additionally we also share the code of our baseline training for the sake of reproducibility. For more information please see README in [baseline directory](baseline/)


# 3. Citation
Please cite us as:
```python
@inproceedings{Wessel2023,
title = {Introducing MBIB - the first Media Bias Identification Benchmark Task and Dataset Collection},
author = {Martin Wessel and Tomas Horych and Terry Ruas and Akiko Aizawa and Bela Gipp and Timo Spinde},
url = {https://media-bias-research.org/wp-content/uploads/2023/04/Wessel2023Preprint.pdf
},
doi = {https://doi.org/10.1145/3539618.3591882},
isbn = {978-1-4503-9408-6/23/07},
year = {2023},
date = {2023-07-01},
urldate = {2023-07-01},
booktitle = {Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’23)},
publisher = {ACM},
address = {New York, NY, USA},
abstract = {Although media bias detection is a complex multi-task problem, there is, to date, no unified benchmark grouping these evaluation tasks. We introduce the Media Bias Identification Benchmark (MBIB), a comprehensive benchmark that groups different types of media bias (e.g., linguistic, cognitive, political) under a common framework to test how prospective detection techniques generalize. After reviewing 115 datasets, we select nine tasks and carefully propose 22 associated datasets for evaluating media bias detection techniques. We evaluate MBIB using state-of-the-art Transformer techniques (e.g., T5, BART). Our results suggest that while hate speech, racial bias, and gender bias are easier to detect, models struggle to handle certain bias types, e.g., cognitive and political bias. However, our results show that no single technique can outperform all the others significantly.We also find an uneven distribution of research interest and resource allocation to the individual tasks in media bias. A unified benchmark encourages the development of more robust systems and shifts the current paradigm in media bias detection evaluation towards solutions that tackle not one but multiple media bias types simultaneously.}
}
```
