import numpy as np
from sentence_transformers import SentenceTransformer, util


def softmax(x, temperature=1.0):
    """Compute softmax(x) with a temperature."""
    x = np.array(x)
    x = x / temperature
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


def filter(query, paragraphs, encoder=None, top_k=5):
    '''
    Filter paragraphs by similarity to query.

    Args:
        query (str): Query string.
        paragraphs (list): List of paragraphs to filter.
        encoder (sentence_transformers.SentenceTransformer): SentenceTransformer to use.
        top_k (int): Number of paragraphs to return.

    Returns:
        (list): List of paragraphs.
    '''
    if not encoder:
        encoder = SentenceTransformer('all-MiniLM-L6-v2')

    query_emb = encoder.encode([query])[0]
    paragraph_embs = encoder.encode(paragraphs)

    results = util.semantic_search(query_emb, paragraph_embs)[0]
    results = [e['corpus_id'] for e in results[:top_k]]
    results = [paragraphs[i] for i in results]
    return results
