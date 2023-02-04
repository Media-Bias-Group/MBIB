import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/072_Liar'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'072-liar_dataset.csv')

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

files = [ele for ele in os.listdir(raw_path) if ".tsv" in ele]
id = 0
ds_lst = []
for entry in files:
    with open(os.path.join(raw_path, entry), 'r', errors= 'replace') as f:
        file = f.readlines()
    file_split = [ele.split("\t") for ele in file]
    ds_sub_lst = []
    for i in file_split:
        text = i[2]
        if i[1] in ['half-true', 'mostly-true', 'barely-true', 'true']:
            label = 0
        elif i[1] in ['false', 'pants-fire']:
            label = 1
        else:
            raise ValueError
        labels_lst = {'true': 0, 'mostly-true': 1, 'half-true': 2, 'barely-true': 3, 'false': 4, 'pants-fire': 5}
        ds_sub_lst.append([id, prepare_text(text), label, labels_lst[i[1]]])
        id += 1
    ds_lst.extend(ds_sub_lst)
df = pd.DataFrame(ds_lst, columns = ['id', 'text', 'label', 'label_multiclass'])

df.to_csv(clean_path,index=False)
