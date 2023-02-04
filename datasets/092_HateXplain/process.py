import os
import pandas as pd
from datasets.data_utils import prepare_text
import json
from collections import Counter

project_path = os.getcwd()
local_path = 'datasets/092_HateXplain'
raw_path = os.path.join(project_path,local_path,'raw/dataset.json')
clean_path = os.path.join(project_path,local_path,'092-HateXplain.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

with open(raw_path, 'r') as fd:
        ds_json = json.load(fd)

for key in ds_json.keys():
    annotators = ds_json[key]['annotators']
    slst = [ele['label'] for ele in annotators]
    words_count = Counter(slst)
    if words_count['normal'] >= 2:
        label = 0
        category = 0 # NEUTRAL
    elif words_count['offensive'] >= 2:
        label = 0
        category = 2 # OFFENSIVE
    elif words_count['hatespeech'] >= 2:
        label = 1
        category = 1 # HATESPEECH
    else:
        label = 0 # put it into category null since I didn't count offensive as hatespeech
        category = 3 # UNDECIDED
    ds_json[key]['label'] = label
    ds_json[key]['category'] = category
    ds_json[key]['text'] = " ".join(ds_json[key]['post_tokens'])

df_hatexplain = pd.DataFrame(ds_json).transpose()
df = df_hatexplain.loc[:,['text', 'label', 'category']]
df['text'] = df['text'].apply(prepare_text)
df['id'] = range(len(df))
df.to_csv(clean_path)