from pathlib import Path
import pickle
from src.util import filter
from src.abduction import infer
from src.baselines import infer_embs, infer_nli
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import CrossEncoder, SentenceTransformer
import pandas as pd
from tqdm import tqdm


df = pd.read_csv(Path('..') / 'data' / 'tweets' / 'tweets.csv')
users = ['nabla_theta', 'slatestarcodex', 'stuhlmueller', 'ESYudkowsky', 'ben_j_todd',
         'ch402', 'willmacaskill', 'hardmaru', 'kenneth0stanley', 'RichardMCNgo']

emb_model = SentenceTransformer('all-MiniLM-L6-v2')
# nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')
lm_model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-2.7B')
lm_tok = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-2.7B')
print('(*) Loaded models')

for user in tqdm(users):
    claim_tweets = df[df['username'] == user][pd.notna(
        df['extracted_claim'])][pd.notna(df['negated_claim'])]

    for approach in ['lm']:  # ['embs', 'nli_relative', 'nli_absolute', 'lm']:
        print(user, approach)
        aggregate = []
        artifact_path = Path(
            '..') / 'data' / 'tweets_artifacts' / 'lm' / (user + '.pkl')

        for idx, row in claim_tweets.iterrows():
            other_tweets = df[df['username'] ==
                              user][df['extracted_claim'] != row['extracted_claim']]['tweet'].values

            selection = filter(
                row['extracted_claim'], other_tweets, emb_model, top_k=5)
            print('(*) Filtered paragraphs')
            probs = []

            for tweet in selection:
                if approach == 'embs':
                    probs += [infer_embs(tweet, [row['extracted_claim'],
                                                 row['negated_claim']], encoder=emb_model)[0]]
                elif approach == 'nli_absolute':
                    probs += [infer_nli(tweet,
                                        [row['extracted_claim']], mode='absolute')[0]]
                elif approach == 'nli_relative':
                    probs += [infer_nli(tweet, [row['extracted_claim'],
                                        row['negated_claim']], mode='relative')[0]]
                elif approach == 'lm':
                    probs += [infer(tweet, [row['extracted_claim'], row['negated_claim']],
                                    model=lm_model, tokenizer=lm_tok, return_components=True)]

            aggregate += [probs]
        pickle.dump(aggregate, open(artifact_path, 'wb'))
