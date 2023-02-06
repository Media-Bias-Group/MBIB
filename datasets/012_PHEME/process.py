import os
import pandas as pd
from datasets.data_utils import prepare_text
from datasets.data_utils import TweetLoader
import json

project_path = os.getcwd()
local_path = 'datasets/012_PHEME'
raw_path = os.path.join(project_path,local_path,'raw/all-rnr-annotated-threads')
clean_path = os.path.join(project_path,local_path,'012-Pheme.csv')

if not os.path.isdir(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.DataFrame(columns= ['tweetID', 'text', 'label', 'rumour'])
tweet = TweetLoader()
topics = [ele for ele in os.listdir(raw_path) if '.' not in ele]



for topic in topics:
    articles_nr = [ele for ele in os.listdir(os.path.join(raw_path, topic, 'non-rumours')) if '.' not in ele] # List of all non-roumor articles
    tweets_non_rumour = tweet.fetch_list(articles_nr) # pandas Dataframe, used Tomasz's class
    tweets_non_rumour['label'] = 0 # since there are no veracity labels for non-rumours, assumed to be true
    tweets_non_rumour['rumour'] = 0
    df = pd.concat([df, tweets_non_rumour])

    # rumours
    articles_r = [ele for ele in os.listdir(os.path.join(raw_path, topic, 'rumours')) if '.' not in ele]
    tweets_rumour = tweet.fetch_list(articles_r)
    # to get the labels the annotation.json need to be parsed:
    label = []
    for article in tweets_rumour.loc[:]['tweetID']:
        with open(os.path.join(raw_path, topic, 'rumours', str(article), 'annotation.json'), 'r') as f:
            annotation = json.load(f)
        try:
            veracity = annotation['true']
            if veracity == 0 or veracity == str(0):
                label.append(1)
            elif veracity == 1 or veracity == str(1):
                label.append(0)
            else:
                print(annotation)
                raise ValueError
        except KeyError: # If the truth is undecided
            label.append(2)
    tweets_rumour['label'] = label
    tweets_rumour['rumour'] = 1
    df = pd.concat([df, tweets_rumour])
df['text'] = df['text'].apply(prepare_text)
df.reset_index(inplace=True)
df['id'] = df.index
df.to_csv(clean_path)