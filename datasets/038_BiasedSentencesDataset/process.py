import os
import pandas as pd
from datasets.data_utils import prepare_text
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

project_path = os.getcwd()
local_path = 'datasets/038_BiasedSentencesDataset'
raw_path = os.path.join(project_path,local_path,'raw/Sora_LREC2020_biasedsentences.csv')
clean_path = os.path.join(project_path,local_path,'038-BiasedSentencesDataset.csv')

if not os.path.isfile(raw_path):
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df_original = pd.read_csv(raw_path)
df_text = df_original.groupby('id_article').min().reset_index()
df_average_label = df_original.groupby('id_article').mean()
ds = []
article_id = 0
for row in range(len(df_text)):
    sentence_id = 0
    for sent_index in range(20):
        category = df_average_label.loc[row+1, str(sent_index)]
        if category < 1.5:
            label = 0
        elif category >= 1.5:
            label = 1
        else:
            raise ValueError
        text = prepare_text(str(df_text.loc[row, 's' + str(sent_index)])[4:])
        id = str(article_id) + '-' + str(sentence_id)
        if text != "":  # Some articles are shorter than 19 sentences
            sub_lst = [id, text,  label, category-1] # original scale goes from 1 to 4
            ds.append(sub_lst)
        sentence_id += 1
    article_id += 1
df = pd.DataFrame(ds, columns=['id', 'text', 'label', 'category'])
df.to_csv(clean_path)