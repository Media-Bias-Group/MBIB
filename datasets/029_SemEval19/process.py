import os
import pandas as pd
from datasets.data_utils import prepare_text
from bs4 import BeautifulSoup as bs

project_path = os.getcwd()
local_path = 'datasets/029_SemEval19'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'029-SemEval2019.csv')

articles = [os.path.join(raw_path, 'articles-training-byarticle-20181122.xml'), os.path.join(raw_path, 'articles-test-byarticle-20181207.xml')]
ground_truth = [os.path.join(raw_path, 'ground-truth-training-byarticle-20181122.xml'), os.path.join(raw_path, 'ground-truth-test-byarticle-20181207.xml')]

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

df_final = pd.DataFrame(columns=['id', 'text', 'label'])
for z in range(len(articles)):
    with open(articles[z], 'r', errors='replace') as f:
        file = f.read()
    bs_file = bs(file, 'xml')
    ds = []
    for article in bs_file.find_all('article'):
        article_id = article.get('id')
        sentences = [prepare_text(ele.get_text()) for ele in article.find_all('p')]
        for k, sentence in enumerate(sentences):
            ds.append([str(article_id)+'-'+str(k), article_id, sentence, len(sentence.split())])
    df_articles = pd.DataFrame(ds, columns= ['id', 'article_id', 'text', 'wordcount'])
    with open(ground_truth[z], 'r', errors='replace') as g:
        file2 = g.read()
    bs_file_label = bs(file2, 'xml')
    ds_label = []
    for labels in bs_file_label.find_all('article'):
        article_id = labels.get('id')
        hyperpartisan = labels.get('hyperpartisan')
        if hyperpartisan == "true":
            label = 1
        elif hyperpartisan == "false":
            label = 0
        ds_label.append([article_id, label])
    df_labels = pd.DataFrame(ds_label, columns= ['article_id', 'label'])
    df = pd.merge(df_articles, df_labels, on= 'article_id', how= 'inner')
    df.drop('wordcount', axis=1, inplace=True)
    df.drop('article_id', axis=1, inplace=True)
    df_final = pd.concat([df_final, df])
df_final.to_csv(clean_path)