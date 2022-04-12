import numpy as np


def softmax(x, temperature=1.0):
    """Compute softmax(x) with a temperature."""
    x = np.array(x)
    x = x / temperature
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
