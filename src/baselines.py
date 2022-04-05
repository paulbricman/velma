from sentence_transformers import CrossEncoder, SentenceTransformer
from sentence_transformers.util import semantic_search
import torch


def infer_nli(context, statements, nli=None):
    '''
    Baseline inference by abduction using vanilla deductive NLI.

    Args:
        context (str): Background context treated as premise in abduction.
        statements (list): List of statements to rank by likelihood of being entailed.
        nli (sentence_transformers.CrossEncoder): CrossEncoder to use.

    Returns:
        (list): List of entailment probabilities for each statement.
    '''
    if not nli:
        nli = CrossEncoder('cross-encoder/nli-deberta-v3-base')

    pairs = [(context, e) for e in statements]
    scores = nli.predict(pairs, apply_softmax=True)
    scores = [e[1] for e in scores]

    return scores


def infer_embs(context, statements, encoder=None):
    '''
    Baseline inference by abduction using semantic similarity between context and statements.

    Args:
        context (str): Background context treated as premise in abduction.
        statements (list): List of statements to rank by semantic similarity.
        encoder (sentence_transformers.SentenceTransformer): SentenceTransformer to use.

    Returns:
        (list): List of semantic similarity probabilities for each statement.
    '''
    if not encoder:
        encoder = SentenceTransformer('all-MiniLM-L6-v2')

    context_emb = encoder.encode(context)
    statement_embs = encoder.encode(statements)

    results = semantic_search(context_emb, statement_embs)[0]
    results = sorted(results, key=lambda x: x['corpus_id'])
    results = [e['score'] for e in results]
    results = torch.softmax(torch.tensor(results), dim=0)

    return results
