# 066 BigNews
contains a crawl of articles classified by the media outlet’s political leaning as defined by allsites.com. The 3.689.229
articles were classified as neutral or left/right-leaning. The label for left/right was
concatenated to one bias label to binarize it. The articles were split on the sentence
level to make the length compatible with the rest of the data. The resulting data,
however, is only distantly labeled.

## Original repository:
https://github.com/launchnlp/POLITICS

## Citation:
```
@inproceedings{liu-etal-2022-politics,
    title = "{POLITICS}: Pretraining with Same-story Article Comparison for Ideology Prediction and Stance Detection",
    author = "Liu, Yujian  and
      Zhang, Xinliang Frederick  and
      Wegsman, David  and
      Beauchamp, Nicholas  and
      Wang, Lu",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2022",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    pages = "1354--1374",
}
```