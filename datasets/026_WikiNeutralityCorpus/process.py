import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/026_WikiNeutralityCorpus'
raw_path = os.path.join(project_path,local_path,'raw/biased.full')
clean_path = os.path.join(project_path,local_path,'026-WNC.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

with open(raw_path, "r", errors='replace') as fd:
    file = fd.readlines()
file_split = [ele.split("\t") for ele in file]
id = 0
ds_lst = []
for i in file_split:
    biased_text = i[3]
    nonbiased_text = i[4]
    biased_id = str(id) + ("-A")
    nonbiased_id = str(id) + ("-B")
    ds_lst.append([biased_id, prepare_text(biased_text), 1])
    ds_lst.append([nonbiased_id, prepare_text(nonbiased_text), 0])
    id += 1
df = pd.DataFrame(ds_lst, columns = ['id', 'text', 'label'])
df.to_csv(clean_path)