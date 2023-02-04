import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/003_WikiNPOV'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'003-NPOV.csv')
files = ['statements_biased','statements_neutral_type_balanced','statements_neutral_featured','statements_neutral_cw-hard']

#
if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

ds_lst = []
id = 0
for filename in files:
    with open(os.path.join(raw_path,filename), errors= 'replace') as fd:
        file = fd.readlines()
    if 'biased' in filename:
        label = 1
    else:
        label = 0

    for j in file:
        row = [id, prepare_text(j), label]
        ds_lst.append(row)
        id += 1
df = pd.DataFrame(ds_lst, columns= ['id', 'text', 'label'])
df.to_csv(clean_path)