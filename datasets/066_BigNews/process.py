import os
import pandas as pd
from datasets.data_utils import prepare_text
from csv import writer
import ijson


project_path = os.getcwd()
local_path = 'datasets/066_BigNews'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'066-BigNews-balanced.csv')

path_center = os.path.join(raw_path,'BIGNEWSBLN_train_center.json')
path_left = os.path.join(raw_path,'BIGNEWSBLN_train_left.json')
path_right = os.path.join(raw_path,'BIGNEWSBLN_train_right.json')

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df = pd.DataFrame(columns= ['text', 'label', 'category'])
df.index.name='id'
csv_path = clean_path
df.to_csv(csv_path)
id = 0
with open(csv_path, 'a', newline='') as f_object:
    for file, label, category in [(path_center, 0, 0), (path_left, 1, 1), (path_right, 1, 2)]:
        with open(file, 'rb') as f:
            writer_object = writer(f_object)
            for i in ijson.items(f, "item"):
                text = i['text']
                id_add = 0
                for sentence in text:
                    final_id = str(id) + '-' + str(id_add)
                    sent = prepare_text(sentence)
                    writer_object.writerow([final_id, sent, label, category])
                    id_add += 1
                id += 1

#balance & subsamle
df = pd.read_csv(clean_path)

df0 = df[df['label'] == 0].sample(n=250000, random_state=42)
df1 = df[df['label'] == 1].sample(n=250000, random_state=42)
df_merged = pd.concat([df0, df1], ignore_index=True, sort=False)
df_merged.to_csv(clean_path)