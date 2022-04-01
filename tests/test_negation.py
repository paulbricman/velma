from src.negation import negate


def test_easy():
    assert 'This is not how I want news to look like.' in negate(
        'This is how I want news to look like.')
