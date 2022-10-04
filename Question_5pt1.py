import numpy as np
import math
from Program_A import approximator
import Program_B


# Zeros will be from numerator and poles from denominator
# Care taken when these roots align

def find_coefficient(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1/2
    numerator = (-1)**(k-1) * math.factorial(2*k - 3)
    denominator = 2**(2*k - 2) * math.factorial(k) * \
                        math.factorial(k-2)
    return numerator / denominator



def generate_approximant(L, M):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(L + M + 1):
        c_vector = np.append(c_vector, 
                find_coefficient(i))
    approximant = approximator(c_vector, L, M)
    return approximant


def find_poles(numerator_coefficients, 
    denominator_coefficients):
    poles_list = []
    denominator_roots = Program_B.find_roots\
                        (denominator_coefficients)
    numerator_roots = Program_B.find_roots\
                        (numerator_coefficients)
    checked_roots = {}  # will add the roots from numerator
    # checked already to this set

    for zero in denominator_roots:
        if zero in checked_roots:
            pass
        else:
            denominator_multiplicity = \
                denominator_roots.count(zero)
            numerator_multiplicity = \
                numerator_roots.count(zero)
            if denominator_multiplicity - \
                numerator_multiplicity > 0:
                poles_list.append(zero)
            checked_roots.add(zero)

    return poles_list



def find_zeros(numerator_coefficients, 
    denominator_coefficients):
    zeros_list = []
    denominator_roots = Program_B.find_roots\
                        (denominator_coefficients)
    numerator_roots = Program_B.find_roots\
                        (numerator_coefficients)
    checked_roots = {} 

    for zero in denominator_roots:
        if zero in checked_roots:
            pass
        else:
            denominator_multiplicity = \
                denominator_roots.count(zero)
            numerator_multiplicity = \
                numerator_roots.count(zero)
            if numerator_multiplicity - \
                denominator_multiplicity > 0:
                zeros_list.append(zero)
            checked_roots.add(zero)

    return zeros_list