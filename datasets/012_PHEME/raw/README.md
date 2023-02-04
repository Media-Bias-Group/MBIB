1. Download data from [here](https://figshare.com/articles/dataset/PHEME_dataset_for_Rumour_Detection_and_Veracity_Classification/6392078) and extract into this folder.
2. In order to process the data, you need to have an developer API access to Twitter. You can get the access for free. After you are granted the access, put the values of:
    - API_KEY
    - API_KEY_SECRET
    - BEARER_TOKEN
    - TOKEN
    - TOKEN_SECRET
  
    Into this project config.py file.
    The class TweetLoader that uses these information in order to access tweet texts can be found in `/datasets/data_utils.py`