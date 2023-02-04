import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/010_BABE'
raw_path = os.path.join(project_path,local_path,'raw/final_labels_SG2.xlsx')
clean_path = os.path.join(project_path,local_path,'010-babe.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df_original = pd.read_excel(raw_path)
df = pd.DataFrame()
df['text'] = df_original['text'].apply(lambda x: prepare_text(x))
df['label'] = df_original['label_bias']
df.loc[df['label'] == 'Biased', 'label'] = 1
df.loc[df['label'] == 'Non-biased', 'label'] = 0
df.loc[df['label'] == 'No agreement', 'label'] = 2
df['id'] = df.index
df.to_csv(clean_path)