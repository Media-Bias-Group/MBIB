import re
import pandas as pd
import tweepy
from tqdm.auto import tqdm
import os

from config import API_KEY, API_KEY_SECRET, BEARER_TOKEN, TOKEN, TOKEN_SECRET


class TweetLoader:
    """Class for fetching tweets identified by tweetID via Twitter API."""

    def __init__(self):
        """Initialize tweet loader."""
        self.client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_KEY_SECRET,
            access_token=TOKEN,
            access_token_secret=TOKEN_SECRET,
            wait_on_rate_limit=True,
        )
        self.TWEET_LIMIT = 100

    def fetch_single_tweet(self, tweetID: str) -> str:
        """Fetch single tweet identified by tweetID."""
        tweet = self.client.get_tweets(ids=[tweetID])

        if not tweet.errors:
            return tweet.data[0].text
        else:
            return tweet.errors[0]["title"]

    def fetch_list(self, ids_list: list) -> pd.DataFrame:
        """Fetch list of tweet ids."""
        tweets_lst = []

        # batches according to maximal twitter api limit
        for tweet_batch in tqdm(
            self._batch(ids_list, batch_size=self.TWEET_LIMIT), total=len(ids_list) / self.TWEET_LIMIT
        ):
            tweets = self.client.get_tweets(ids=tweet_batch)

            if tweets.data is not None:
                tweets_lst.extend(tweets.data)

        return self._tweets_to_pandas(tweets_lst)

    def _tweets_to_pandas(self, lst) -> pd.DataFrame:
        """Fast way to load data into dataframe."""
        row_list = []
        for row in lst:
            dict1 = {}
            dict1.update({"tweetID": row.id, "text": row.text})
            row_list.append(dict1)

        return pd.DataFrame(row_list, columns=["tweetID", "text"])

    def _batch(self, lst, batch_size):
        """Create batches of fixed size from list of arbitrary length."""
        lst_length = len(lst)
        for idx in range(0, lst_length, batch_size):
            yield lst[idx : min(idx + batch_size, lst_length)]

def prepare_text(text):
        text = re.sub(r"@[A-Za-z0-9_]+", ' ', text) # remove @user
        text = re.sub(r"https?://[A-Za-z0-9./]+", ' ', text) # remove links
        text = re.sub(r"[^a-zA-z.!?'0-9]", ' ', text) # remove smileys
        text = re.sub('[^A-Za-z0-9]+', ' ', text) # remove any other special characters
        text = re.sub('#', '', text) # remove hash sign
        text = re.sub('\t', ' ',  text) # remove tab
        text = re.sub(r" +", ' ', text) # remove multiple whitespaces
        text = re.sub(r"linebreak", '', text)  # remove linebreaks
        return text

class MBIBDataLoader:
    def __init__(self):
        self.project_path = os.getcwd()
        self.datasets_path = os.path.join(self.project_path,'datasets')
        # mapping for tasks. Each task consists of several datasets
        self.category_ids = {'0': ['003', '010', '026', '049', '075', '035', '009', '038'],
                             '1': ['066', '072'],
                             '2': ['019', '076'],
                             '3': ['040', '075', '087', '092'],
                             '4': ['075', '105', '106', '107'],
                             '5': ['075', '034', '113', '110'],
                             '6': ['072', '012', '025'],
                             '7': ['049', '066', '029']}
        self.category_id_to_name = {'0':'linguistic-bias',
                                    '1':'cognitive-bias',
                                    '2':'text-level-bias',
                                    '3':'hate-speech',
                                    '4':'gender-bias',
                                    '5':'racial-bias',
                                    '6':'fake-news',
                                    '7':'political-bias'}
    


    def load_balanced_sample(self,category_ids):
        """
        Draws a random sample based on the smaller available label.
        """
        df = self.get_category_data(category_ids)
        df = df.drop_duplicates('text', keep='first')
        df_wo2 = df[df['label'] != 2] # drop label 2
        k=min(len(df[df['label'] == 1]), len(df[df['label'] == 0]))
        grouped = df_wo2.groupby('label')
        df_balanced = grouped.apply(lambda x: x.sample(n=k, random_state=42))
        return df_balanced

    def load_data(self, directories: list):
        """
        Loads the data from the internal file structure for now, should change here for the automatic downloading
        Assigns new unique id to every datapoint: Dataset_id-Prior_id
        """
        df = pd.DataFrame(columns=['id', 'text', 'label'])
        for dataset_id,data_dir in directories:
            path = os.path.join(self.datasets_path, data_dir)
            file_path = self.get_clean_filepath_from_dir(path)
            if file_path is None:
                print("Skipping " + dataset_id)
                continue
            df_sub = pd.DataFrame()
            df_file = pd.read_csv(file_path)
            df_file['nr'] = str(dataset_id)
            df_file['new_id'] = df_file['nr'] + '-' + df_file['id'].astype(str)
            df_sub['id'], df_sub['text'], df_sub['label'] = df_file['new_id'], df_file['text'], df_file['label']
            df_sub['dataset_id'] = df_file['nr']
            df = pd.concat([df, df_sub], axis=0)
        return df
    
    def get_clean_filepath_from_dir(self,dir:str):
        """Helper function for getting the clean .csv file which doesnt
            have unified naming. """
        contents = os.listdir(dir)
        for cont in contents:
            if '.csv' in cont:
                return os.path.join(dir,cont)
        return None

    def get_category_data(self,category_ids):
        """
        Loads the data from the local file path,
        sorts files by category ids and combines them to one df
        """
        contents = os.listdir(self.datasets_path)
        category_files = []
        for id in category_ids:
            for cont in contents:
                if str(id) in cont:
                    category_files.append((id, cont))
        df = self.load_data(category_files)
        return df

    def create_all_categories(self):
        for cat_idx, category_ids in self.category_ids.items():
            df_balanced = self.load_balanced_sample(category_ids)
            df_balanced.to_csv(os.path.join(self.datasets_path,'mbib-aggregated',self.category_id_to_name[cat_idx] + '.csv'),index=False)