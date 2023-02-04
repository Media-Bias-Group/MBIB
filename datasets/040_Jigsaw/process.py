import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/040_Jigsaw'
raw_path = os.path.join(project_path,local_path,'raw/all_data.csv')
clean_path = os.path.join(project_path,local_path,'040-Jigsaw-balanced.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df_original = pd.read_csv(raw_path)
df = pd.DataFrame()
df['text'] = df_original['comment_text'].apply(lambda x: prepare_text(str(x)))
df['label'] = df_original['toxicity']
df['label_float']  = df_original['toxicity']
df.loc[df['label'] >= 0.5, 'label'] = 1
df.loc[df['label'] < 0.5, 'label'] = 0
df['label'] = df['label'].astype(int)
df['id'] = df.index

df0 = df[df['label'] == 0].sample(n=df.label.value_counts().min(), random_state=42)
df1 = df[df['label'] == 1]

df_merged = pd.concat([df0, df1], ignore_index=True, sort=False)

df.to_csv(clean_path)