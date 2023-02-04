import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/087_OnlineHarassmentCorpus'
raw_path = os.path.join(project_path,local_path,'raw/onlineHarassmentDataset.tdf')
clean_path = os.path.join(project_path,local_path,'087-OnlineHarassment.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

with open(raw_path, errors= 'replace') as fd:
    file = fd.readlines()
    file_split = [ele.split("\t") for ele in file]
id = 0
ds = []
for i in file_split[1:]:
    try:
        if i[1] == "H":
            label = 1
            ds.append([id, prepare_text(i[2]), label])
        elif i[1] == "N":
            label = 0
            ds.append([id, prepare_text(i[2]), label])
        else:
            if i[2] == "H":
                label = 1
                ds.append([id, prepare_text(i[5]), label])
            elif i[2] == "N":
                label = 0
                ds.append([id, prepare_text(i[5]), label])
            else:
                pass # Some entries don't have a label, checked all of them
    except IndexError:
        pass # There seem to be empty rows that otherwise run out of index
    id += 1
df = pd.DataFrame(ds, columns= ['id', 'text', 'label'])
df.to_csv(clean_path)