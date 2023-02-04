import os
import pandas as pd
from datasets.data_utils import prepare_text
import numpy as np

project_path = os.getcwd()
local_path = 'datasets/076_CAD'
raw_path = os.path.join(project_path,local_path,'raw/cad_v1_1.tsv')
clean_path = os.path.join(project_path,local_path,'076-ContextualAbuse.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

#word_count = []
categories = {"Neutral": 0, "AffiliationDirectedAbuse": 1, "Slur": 2, "PersonDirectedAbuse": 3, "IdentityDirectedAbuse": 4, "CounterSpeech": 5}
with open(raw_path, "r", errors='replace') as fd:
    file = fd.readlines()
file_split = [ele.split("\t") for ele in file]
id = 0
ds_lst = []
for i in file_split[1:]:
    text = i[-1]
    #split_text = text.split(' ')
    #if len(split_text) > 1:
        # word_count.append(len(split_text)-1)
    if i[9] == "Neutral":
        label = 0
    elif i[9] in ["AffiliationDirectedAbuse", "Slur", "PersonDirectedAbuse", "IdentityDirectedAbuse", "CounterSpeech"]:
        label = 1
    else:
        print(i[9])
        raise ValueError
    multi_class_label = categories[i[9]]
    ds_lst.append([id, prepare_text(text), label, multi_class_label])
    id += 1
df = pd.DataFrame(ds_lst, columns = ['id', 'text', 'label', 'category'])
df['text'].replace(' ', np.nan, inplace=True)
df = df.dropna()
df.to_csv(clean_path)
