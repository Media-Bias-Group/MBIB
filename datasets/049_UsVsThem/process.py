import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/049_UsVsThem'
raw_path = os.path.join(project_path,local_path,'raw/Reddit_dataset.csv')
clean_path = os.path.join(project_path,local_path,'049-USvsThem.csv')


df_original = pd.read_csv(raw_path)
df = pd.DataFrame()
df['text'] = df_original['body'].apply(lambda x: prepare_text(x))
df['label'] = df_original['is_Disc_Crit_encoded']
df['usVSthem_scale'] = df_original['usVSthem_scale']
df['id'] = df.index
df.to_csv(clean_path)