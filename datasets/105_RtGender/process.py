import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/105_RtGender'
raw_path = os.path.join(project_path,local_path,'raw/annotations.csv')
clean_path = os.path.join(project_path,local_path,'105-rtgender.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.read_csv(raw_path)

dict_label = {'Neutral' : 0, 'Positive' : 1, 'Negative' : 1, 'Mixed' : 1}
dict_category = {'Neutral' : 0, 'Positive' : 1, 'Negative' : 2, 'Mixed' : 3}


df['id'] = pd.DataFrame(range(len(df))) + 1
df['text'] = df['post_text'].astype('string') + df['response_text'].astype('string')
df['text'] = df['text'].apply(str).apply(prepare_text)

df['label'] = df['sentiment']
df['category'] = df['sentiment']
df['label'] = df['label'].map(dict_label)

df = df.reindex(columns=['id','text','label','category','source','op_gender','relevance'])
df.to_csv(clean_path)