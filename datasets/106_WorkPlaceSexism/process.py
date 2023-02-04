import os
import pandas as pd
from datasets.data_utils import prepare_text

project_path = os.getcwd()
local_path = 'datasets/106_WorkPlaceSexism'
raw_path = os.path.join(project_path,local_path,'raw/ISEP Sexist Data labeling.xlsx')
clean_path = os.path.join(project_path,local_path,'106-workplacesexism.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.read_excel(raw_path)

df['id'] = pd.DataFrame(range(len(df))) + 1
df['text'] = df['Sentences']
df['text'] = df['text'].apply(str).apply(prepare_text)

df['label'] = df['Label']

df = df.reindex(columns=['id','text','label'])
df.to_csv(clean_path)