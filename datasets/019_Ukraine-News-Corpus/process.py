import os
import pandas as pd
from datasets.data_utils import prepare_text
import json

project_path = os.getcwd()
local_path = 'datasets/019_Ukraine-News-Corpus'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'019-MultidimensionalDataset.csv')

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

files = [ele for ele in os.listdir(raw_path) if '.json' in ele]

article_id = 0
ds_lst = []
for filename in files:
    with open(os.path.join(raw_path, filename)) as fd:
        article = json.load(fd)
        sentences = article['sentences']
    sentence_id = 0
    for i in sentences:
        final_id = str(article_id) + '-' + str(sentence_id)  # so every sentence can be traced back to the article it belongs to
        text = prepare_text(i['content'])
        avg_subjectivity = i['subjectivity']['score']['avg']
        maj_subjectivity = i['subjectivity']['score']['maj']
        avg_hidden = i['hidden_assumptions']['score']['avg']
        maj_hidden = i['hidden_assumptions']['score']['maj']
        avg_bias_west = i['bias']['score']['pro-west']['avg']
        maj_bias_west = i['bias']['score']['pro-west']['maj']
        avg_bias_russia = i['bias']['score']['pro-russia']['avg']
        maj_bias_russia = i['bias']['score']['pro-russia']['maj']

        if 1.5 <= maj_subjectivity <= 3 or 1.5 <= maj_hidden <= 3 or 1.5 <= maj_bias_west  <= 3 or 1.5 <= maj_bias_russia  <= 3:  # turns out majority votes can actually end up being floats
            label = 1
        elif 0 <= maj_subjectivity < 1.5 and 0 <= maj_hidden < 1.5 and 0 <= maj_bias_west  < 1.5 and 0 <= maj_bias_russia  < 1.5:
            label = 0
        else: # just a check
            raise ValueError
        ds_lst.append([final_id, text, label, avg_subjectivity, maj_subjectivity, avg_hidden, maj_hidden, avg_bias_west, maj_bias_west, avg_bias_russia, maj_bias_russia])
        sentence_id += 1
    article_id += 1
df = pd.DataFrame(ds_lst, columns = ['id', 'text', 'label', 'average_subjectivity', 'majority_subjectivity', 'average_hidden_assumptions', 'majority_hidden_assumptions', 'average_bias_west', 'majority_bias_west', 'average_bias_russia', 'majority_bias_russia'])
df.to_csv(clean_path)