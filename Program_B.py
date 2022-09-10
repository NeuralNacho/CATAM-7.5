import numpy as np


def find_roots(polynomial):
    # polynomial should be a 1D array of coefficients 
    # starting with the leading coefficient
    return np.roots(polynomial)