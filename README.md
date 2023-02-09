# Introducing MBIB - the first Media Bias Benchmark Task and Dataset Collection
![d](img.png)

# 1. Introduction
This repository contains all resources from the paper "Introducing MBIB - the first Media Bias Benchmark Task and Dataset Collection"

# 2. Setup
To use scripts in this repository install the python requirements:
1. For dataset processing
```
pip install -r datasets/requirements.txt
 ```
2. For training a model 
```
pip install -r baseline/requirements.txt
 ```

# 3. Datasets

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

# 4. Baseline

# 5. Citation
Please cite us as:
```
@InProceedings{Spinde2021f,
    title = "Neural Media Bias Detection Using Distant Supervision With {BABE} - Bias Annotations By Experts",
    author = "Spinde, Timo  and
      Plank, Manuel  and
      Krieger, Jan-David  and
      Ruas, Terry  and
      Gipp, Bela  and
      Aizawa, Akiko",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.101",
    doi = "10.18653/v1/2021.findings-emnlp.101",
    pages = "1166--1177",
}
```