import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/110_RacialBias'
raw_path = os.path.join(project_path,local_path,'raw/groundTruth.csv')
clean_path = os.path.join(project_path,local_path,'110-RacialBias.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

ground_truth = pd.read_csv(raw_path,on_bad_lines='skip',encoding='iso-8859-1')
df = pd.DataFrame()
df['text'] = ground_truth['Tweet'].apply(prepare_text)
df['label'] = 1
df['category'] = ground_truth['Type of Racism'] - 1
df['polarity'] = ground_truth['Polarity']
df['id'] = df.index
df.to_csv(clean_path)