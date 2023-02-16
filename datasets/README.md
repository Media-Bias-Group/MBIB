datasets
# Dataset collection
The 22 tasks in this repository were carefully selected out of bigger, more extenstive collection under several criteria.
 
For more details about selection process see the paper.
<br/>Full list of 118 datasets and their meta information can be found [here](https://docs.google.com/spreadsheets/d/1BXcDcnBluSzv1bwwAEpRH61ObXd3Mxf66qsOVxilTXM/edit#gid=0).

![d](../figures/mbib_process.png)








## Files description
* `data_utils.py`
  * Contains `TweetLoader` class that fetches batches or single tweets from TwitterAPI.
  * Contains `MBIBDataLoader` class, that aggregates processed datasets into 8 Tasks. <br/> This class is used by `create_corpus.py` script to create final corpus.
  
