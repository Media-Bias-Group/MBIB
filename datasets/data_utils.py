import re
import pandas as pd
import tweepy
from tqdm.auto import tqdm

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