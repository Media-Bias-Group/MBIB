# 039 Biased Sentences Dataset

is made of 842 sentences from 46 news
articles, manually annotated for bias using crowdsourcing. The news articles are all
about four different events. These events cover various topics such as politics, sports,
and economics. The 4-5 given annotations from different annotators per sentence
were averaged to retrieve a single score. Multiple label classes were concatenated to
form a binary label. For instance, the biased and very biased categories were concatenated to only biased.

## Original repository:
https://github.com/skymoonlight/biased-sents-annotation

## Citation:
```
@ inproceedings{
  title     = {Annotating and Analyzing Biased Sentences in News Articles using Crowdsourcing},
  author    = {Sora Lim, Adam Jatowt, Michael F{\"{a}}rber, and Masatoshi Yoshikawa},
  booktitle = {Proceedings of the Twelveth International Conference on Language Resources
               and Evaluation, {LREC} 2020},
  year      = {2020} 
}
```