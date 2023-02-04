import os
import pandas as pd
from datasets.data_utils import prepare_text
import json

project_path = os.getcwd()
local_path = 'datasets/035_MediaFramesCorpus'
raw_path = os.path.join(project_path,local_path,'raw/mfc_v4.0')
clean_path = os.path.join(project_path,local_path,'035-MFC.csv')

if not os.path.isdir(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

files = [ele for ele in os.listdir(raw_path) if "." not in ele]

id = 0
ds_lst = []
for entry in files:
    with open(os.path.join(raw_path + "/" + entry + "/" + entry + "_labeled.json"), 'r') as fd:
        file = json.load(fd)
    ds_sub_lst = []
    for i in list(file.keys()):
        text = file[i]['text'][18:]
        tone = file[i]['primary_tone']
        if tone == 17 or tone == 19:
            label = 1
            ds_sub_lst.append([id, prepare_text(text), label])
            id += 1
        elif tone == 18:
            label = 0
            ds_sub_lst.append([id, prepare_text(text), label])
            id += 1
        else:  # Filters out the unlabeled entries
            pass
    ds_lst.extend(ds_sub_lst)
df = pd.DataFrame(ds_lst, columns= ['id', 'text', 'label'])
df.to_csv(clean_path)

