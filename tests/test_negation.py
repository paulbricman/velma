from src.negation import gen_negations, filter_negations


def test_gen_negations():
    assert 'Cooking is easy.' in gen_negations(
        'Cooking is hard.')


def test_filter_negations():
    statement = 'Cooking is hard.'
    candidates = ['Cooking is easy.', 'Cooking is difficult.',
                  'Given this, the practice of cooking is absolutely trivial.']
    filtered = filter_negations(statement, candidates)

    assert 'Cooking is easy.' in filtered
    assert 'Cooking is difficult.' not in filtered
    assert 'Given this, the practice of cooking is absolutely trivial.' not in filtered
