import os
import pandas as pd
from datasets.data_utils import prepare_text
import json
import re

project_path = os.getcwd()
local_path = 'datasets/025_FakeNewsNet'
raw_path = os.path.join(project_path,local_path,'raw/Data')
clean_path = os.path.join(project_path,local_path,'025-FakeNewsNet.csv')

if not os.path.isdir(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

article_id = 0
ds = []
for source in os.listdir(raw_path):
    #skip readme
    if source == "README.md":
        continue

    for fr in os.listdir(os.path.join(raw_path, source)):
        for article in os.listdir(os.path.join(raw_path, source, fr)):
            with open(os.path.join(raw_path, source, fr, article)) as fd:
                file = json.load(fd)
            type = file['type']
            if type == 'fake':
                label = 1
            elif type == 'real':
                label = 0
            else:
                raise ValueError
            article_text = file['text']
            sentences = [prepare_text(ele) for ele in re.split(r'[\.!?] ', article_text)]
            for k, sentence in enumerate(sentences):
                ds.append([str(article_id)+'-'+str(k), sentence, label])
            article_id += 1
df = pd.DataFrame(ds, columns=['id', 'text', 'label'])
df.to_csv(clean_path)