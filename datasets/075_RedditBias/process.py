import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/075_RedditBias'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'075-RedditBias.csv')
files = ['reddit_comments_gender_female_processed_phrase_annotated.csv', 'reddit_comments_orientation_lgbtq_processed_phrase_annotated.csv', 'reddit_comments_race_black_processed_phrase_annotated.csv','reddit_comments_religion1_jews_processed_phrase_annotated.csv', 'reddit_comments_religion2_muslims_processed_phrase_annotated.csv']

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.DataFrame(columns= ['text', 'label', 'category'])
for file in files:
    file_path = os.path.join(raw_path,file)
    with open(file_path, errors= 'replace') as f:
        df_original = pd.read_csv(f)
    df_sub = pd.DataFrame()
    df_original = df_original.dropna(subset=['bias_sent']) # dropped all rows that did not have a label
    df_original = df_original[~df_original['bias_sent'].isin(['1 - context needed', 're-state', 'biased?', 'toxic-unrelated', 'fact?', 'question'])]
    df_sub['text'] = df_original['comment'].apply(lambda x: prepare_text(x))
    df_sub['category'] = file
    df_sub['label'] = df_original['bias_sent'].apply(lambda x: int(x))
    
    ## reddit_comments_gender_female_processed_phrase_annotated.csv contains `2` in bias_sent. This is not explained.
    #        print(df_original['bias_sent'].unique())
    df_sub = df_sub[df_sub["label"] != 2]
    
    # strangely the number of observations doesn't 100% align with those in the paper but we couldn't find the reason for that
    df = pd.concat([df, df_sub])

df.index.name='id'
df.to_csv(clean_path)