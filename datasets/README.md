datasets
# Dataset collection
The 22 tasks in this repository were carefully selected out of bigger, more extenstive collection under several criteria.
 For more details about selection process see the paper. Full list of 118 datasets and their meta information can be found [here](https://docs.google.com/spreadsheets/d/1BXcDcnBluSzv1bwwAEpRH61ObXd3Mxf66qsOVxilTXM/edit#gid=0).

![d](../figures/mbib_process.png)


| Bias Type |Total size|Dataset| Data Points|
|-----------|----------|-------|------------|
| Linguistic Bias| 433,677 |Wikipedia NPOV | 11,945|
|| |BABE|3,673|
|| |Wiki Neutrality Corpus| 362,991 |
|| |UsVsThem| 6,863 |
|| |RedditBias | 10,583 |
|| |Media Frames Corpus | 37,622|
|| |BASIL| 1,726|
|| |Biased Sentences |842 |
||
| Cognitive Bias                                  | BIGNEWS \cite{liuPOLITICSPretrainingSamestory2022}                           | 2,331,552            |
|                                                 | Liar Dataset \cite{wangLiarLiarPants2017a}                                   | 12,835               |
|                                                 |                                                                              | 2,344,387* \tnote{*} |
| \multirow{2}{*}{\makecell[l]{Text-Level Context |
|                                                 | Multidimensional Dataset \cite{farberMultidimensionalDatasetBased2020a}      | 2,094                |
|                                                 |                                                                              | 28,329* \tnote{*}    |
| Hate Speech                                     | Kaggle Jigsaw \cite{jigsaw/conversationaiJigsawUnintendedBias2019}           | 1,999,516            |
|                                                 | HateXplain \cite{mathewHateXplainBenchmarkDataset2021a}                      | 20,148               |
|                                                 | RedditBias \cite{barikeriRedditBiasRealWorldResource2021a}                   | 10,583               |
|                                                 | Online Harassment Corpus \cite{golbeckLargeLabeledCorpus2017}                | 20,427               |
|                                                 |                                                                              | 2,050,674* \tnote{*} |
| Gender Bias                                     | RedditBias \cite{barikeriRedditBiasRealWorldResource2021a}                   | 3,000                |
|                                                 | RtGender \cite{voigtRtGenderCorpusStudying2018}                              | 15,351               |
|                                                 | WorkPlace sexism \cite{groszAutomaticDetectionSexist2020}                    | 1,136                |
|                                                 | CMSB \cite{samoryCallMeSexist2020}                                           | 13,634               |
|                                                 |                                                                              | 33,121* \tnote{*}    |
| Racial Bias                                     | RedditBias \cite{barikeriRedditBiasRealWorldResource2021a}                   | 2,620                |
|                                                 | RacialBias \cite{ghoshalRacialBiasTwitter2018}                               | 751                  |
|                                                 |                                                                              | 2,371* \tnote{*}     |
| Fake News                                       | Liar Dataset \cite{wangLiarLiarPants2017a}                                   | 12,835               |
|                                                 | PHEME \cite{zubiagaExploitingContextRumour2017}                              | 5,222                |
|                                                 | FakeNewsNet \cite{shuFakeNewsNetDataRepository2020}                          | 6,337                |
|                                                 |                                                                              | 24,394* \tnote{*}    |
| Political Bias                                  | UsVsThem \cite{huguetcabotUsVsThem2021}                                      | 6,863                |
|                                                 | BIGNEWS \cite{liuPOLITICSPretrainingSamestory2022}                           | 2,331,552            |
|                                                 | SemEval \cite{kieselDataPANSemEval2018}                                      | 9,783                |
|                                                 |                                                                              | 2,348,198* \tnote{*} |




## Files description
* `data_utils.py`
  * Contains `TweetLoader` class that fetches batches or single tweets from TwitterAPI.
  * Contains `MBIBDataLoader` class, that aggregates processed datasets into 8 Tasks. This class is used by `create_corpus.py` script to create final corpus.
  
