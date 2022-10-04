import numpy as np
import matplotlib.pyplot as plt
import math
import Question_1
from Program_A import approximator


def continued_fraction(L, x):
    fraction_term = 0
    for _ in range(2*L):
        fraction_term = x / (2 + fraction_term)
    return 1 + fraction_term

def plot_cont_fraction():
    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)

    L_vector = np.arange(0, 51, 1)

    # vfunc = np.vectorize(continued_fraction)
    # estimate_vector = vfunc(L_vector, 10)

    estimate_vector = []
    for i in range(len(L_vector)):
        estimate_vector.append(continued_fraction(i, 10))
    estimate_vector = np.array(estimate_vector)
    error_vector = estimate_vector - math.sqrt(11)
    print(error_vector)
    log_error = np.log(np.absolute(error_vector))
    plt.plot(L_vector, log_error, color = 'C3')

    plt.xlabel('$L$')
    plt.ylabel('$\ln(Error)$')
    plt.tight_layout()
    plt.show()

def diagonal_approximant(L):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 1):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    approximant = approximator(c_vector, L, L)
    print(math.sqrt(11) - approximant.evaluate_approximant(10))

diagonal_approximant(15)
print( math.sqrt(11) - continued_fraction(15, 10))