from src.negation import negate


def test_easy():
    assert 'Cooking is easy.' in negate(
        'Cooking is hard.')
