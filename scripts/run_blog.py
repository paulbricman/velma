from pathlib import Path
import pickle
from src.util import filter
from src.abduction import infer
from src.baselines import infer_embs, infer_nli
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import CrossEncoder, SentenceTransformer
import pandas as pd
import os
from nltk import sent_tokenize


paragraphs = []
for filename in os.listdir('../data/blog/'):
    with open('../data/blog/' + filename, 'r') as f:
        blog = f.read().split('\n\n')[1:]
        blog = [e for e in blog if len(sent_tokenize(e)) > 2]
        paragraphs.extend(blog)

df = pd.read_csv('~/Downloads/valuations.csv')

emb_model = SentenceTransformer('all-MiniLM-L6-v2')
# nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')
lm_model = AutoModelForCausalLM.from_pretrained('distilgpt2')
lm_tok = AutoTokenizer.from_pretrained('distilgpt2')

print('(*) Loaded models')

for approach in ['lm']:  # ['embs', 'nli_relative', 'nli_absolute', 'lm']:
    aggregate = []

    artifact_path = Path('..') / 'data' / \
        'blog_artifacts' / (approach + '.pkl')
    curr_df = df.copy()
    # if artifact_path.exists():
    #     aggregate = pickle.load(open(artifact_path, 'rb'))
    #     curr_df = df.iloc[len(aggregate):]

    for idx, row in curr_df.iterrows():
        print(approach, idx)
        probs = []
        selection = filter(row['statement'], paragraphs, emb_model, top_k=5)
        print('(*) Filtered paragraphs')

        for paragraph in selection:
            if approach == 'embs':
                probs += [infer_embs(paragraph, [row['statement'],
                                     row['negation']], encoder=emb_model)[0]]
            elif approach == 'nli_absolute':
                probs += [infer_nli(paragraph,
                                    [row['statement']], mode='absolute')[0]]
            elif approach == 'nli_relative':
                probs += [infer_nli(paragraph, [row['statement'],
                                    row['negation']], mode='relative')[0]]
            elif approach == 'lm':
                probs += [infer(paragraph, [row['statement'], row['negation']],
                                model=lm_model, tokenizer=lm_tok, return_components=True)]

        aggregate += [probs]
        pickle.dump(aggregate, open(artifact_path, 'wb'))
