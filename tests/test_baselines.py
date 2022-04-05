from src.baselines import infer_nli, infer_embs
from sentence_transformers import CrossEncoder, SentenceTransformer


def test_nli_baseline():
    nli = CrossEncoder('cross-encoder/nli-deberta-v3-base')

    context = 'Social media is awesome because it allows you to connect with others.'
    statements = [' Facebook is amazing.',
                  ' Facebook is awful.']

    probs = infer_nli(context, statements, nli)
    assert probs[0] > probs[1], statements

    context = 'Being vegan is the way to go. Let\'s save the planet.'
    statements = [' Eating meat is completely ethical.',
                  ' Eating meat is not ethical.']

    probs = infer_nli(context, statements, nli)
    assert probs[1] > probs[0], statements


def test_embs_baseline():
    encoder = SentenceTransformer('all-MiniLM-L6-v2')

    context = 'Social media is awesome because it allows you to connect with others.'
    statements = [' Facebook is amazing.',
                  ' Facebook is awful.']

    probs = infer_embs(context, statements, encoder)
    assert probs[0] > probs[1], statements
