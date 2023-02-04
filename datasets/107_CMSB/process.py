import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/107_CMSB'
raw_path = os.path.join(project_path,local_path,'raw/sexism_data.csv')
clean_path = os.path.join(project_path,local_path,'107-cmsb.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.read_csv(raw_path)

replace_dict = {
    False: 0,
    True: 1
}

df['label'] = df['sexist'].replace(replace_dict)

df['id'] = pd.DataFrame(range(len(df))) + 1
df['text'] = df['text'].apply(str).apply(prepare_text)
df = df.reindex(columns=['id','text','label','toxicity'])
df.to_csv(clean_path)