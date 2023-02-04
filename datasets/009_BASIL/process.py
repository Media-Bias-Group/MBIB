import os
import pandas as pd
from datasets.data_utils import prepare_text
import json
import itertools

project_path = os.getcwd()
local_path = 'datasets/009_BASIL'
raw_path = os.path.join(project_path,local_path,'raw')
clean_path = os.path.join(project_path,local_path,'009-Basil.csv')

if len(os.listdir(raw_path)) == 1:
    print("Raw data of " + local_path.split('/')[1] + " are missing.")
    quit()

def _load_data():
    """Load the raw data of 09_BASIL."""
    articles, annotations = [], []
    for year in range(2010, 2020):
        arts = sorted(os.listdir(os.path.join(raw_path, "articles", str(year))))
        anns = sorted(os.listdir(os.path.join(raw_path, "annotations", str(year))))
        anns_cut = [("").join(ann.split("_ann")) for ann in anns]

        assert arts == anns_cut

        for i, art in enumerate(arts):
            try:
                with open(os.path.join(raw_path, "articles", str(year), art), "r", errors= 'replace') as f:
                    article_data = json.load(f)

                with open(os.path.join(raw_path, "annotations", str(year), anns[i]), "r", errors= 'replace') as f:
                    annotation_data = json.load(f)

                articles.append(article_data)
                annotations.append(annotation_data)
            except json.decoder.JSONDecodeError:
                print("Caught error. Attempted to load an empty file.")

    return articles, annotations

"""Preprocess the raw data of 09_BASIL."""
article_data, annotation_data = _load_data()
observations = []
sent_id = 0
for i, art in enumerate(article_data):
    ann = annotation_data[i]

    paragraphs = art.get("body-paragraphs")  # Now a list of paragraphs
    annotations = ann.get("phrase-level-annotations")  # Now a list of annotations

    # For each paragraph, join the sentences together
    phrases = list(itertools.chain.from_iterable(paragraphs))
    for ann in annotations:
        # The id can be in 2 different formats:
        # "p<prase-id>" or "title"
        id = ann["id"]
        text = ann["txt"]
        bias = ann["bias"]  # Type of bias. (inf=linguistic, lex=lexical)
        quote = ann["quote"]  # Binary, whether phrase is/ contains quote or not.
        aim = ann["aim"]  # direct/ indirect. If indirect, annotations for ...-sentiment are availabe.
        if id == "title":
            phrase = art.get("title")
        else:
            id = int(id.split("p")[-1])
            phrase = phrases[id]

        observation = {"id": sent_id, "text": prepare_text(phrase), "label": 1, "pos": text, "bias_type": bias, "quote": quote, "aim": aim}
        observations.append(observation)
        sent_id += 1

df = pd.DataFrame(observations)
df.to_csv(clean_path)