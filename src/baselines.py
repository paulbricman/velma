from sentence_transformers import CrossEncoder, SentenceTransformer
from sentence_transformers.util import semantic_search
from src.util import softmax


def infer_nli(context, statements, nli=None, mode='relative'):
    '''
    Baseline inference by abduction using vanilla deductive NLI.

    Args:
        context (str): Background context treated as premise in abduction.
        statements (list): List of statements to rank by likelihood of being entailed.
        nli (sentence_transformers.CrossEncoder): CrossEncoder to use.
        mode (str): "relative" yields entailment probs across statement pair,
            while "absolute" yields entailment and contradiction probs for original statement.

    Returns:
        (list): List of probs.
    '''
    assert mode in [
        'relative', 'absolute'], 'Invalid mode, should be "relative" or "absolute".'

    if not nli:
        nli = CrossEncoder('cross-encoder/nli-deberta-v3-base')

    if mode == 'relative':
        pairs = [(context, e) for e in statements]
        scores = nli.predict(pairs)
        scores = softmax([e[1] for e in scores], 0.2)
    elif mode == 'absolute':
        pair = (context, statements[0])
        scores = nli.predict(pair)
        scores = softmax([scores[1], scores[0]], 0.2)

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
    results = softmax(results, 0.2)

    return results
