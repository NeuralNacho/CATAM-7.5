import math
import numpy as np
import matplotlib.pyplot as plt
from Program_A import approximator
import Question_1


def f_1(x):
    return math.sqrt(1 + x)


def series_estimate(N, x):
    sum = 0
    for i in range(N + 1):
        sum += Question_1.find_coefficient(i) * x**i
    return sum


def diagonal_approximant(L, x):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 2):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    approximant = approximator(c_vector, L, L)
    # Can try M = L + 1 in second arg. 
    # Not any improvements
    return approximant.evaluate_approximant(x)


def plot_comparison(N, L):
    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)

    x_vector = np.arange(1,101, 1)
    f_1_vector = np.vectorize(f_1)(x_vector)
    series_vector = np.vectorize(series_estimate)(N, 
                                            x_vector)
    approximant_vector = np.vectorize(diagonal_approximant)\
                                    (L, x_vector)

    plt.figure(1)
    plt.plot(x_vector, f_1_vector, label = '$y=f_{1}(x)$',
        color = 'black')
    label_string = str(L) + ',' + str(L)
    plt.plot(x_vector, approximant_vector, color = 'C1',
        label = '$y=R_{{{}}}(x)$'.format(label_string))
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc = 'best')
    plt.show()

    plt.plot(2)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.rc('font', size = 20)
    plt.xlabel('xlabel', fontsize = 20)
    plt.ylabel('ylabel', fontsize = 20)
    plt.plot(x_vector, series_vector, color = 'C0', label = 
        ' $y=\sum_{{k=0}}^{{{}}}c_{{k}}x^{{k}}$'.format(N))
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.legend(loc = 'best')
    plt.tight_layout()
    # Or just plot the error
    plt.show()


class approximant_investigation:
    def __init__(self, chosen_val1, chosen_val2):
        self.chosen_val1 = chosen_val1
        self.chosen_val2 = chosen_val2
        # chosen_vals are the chosen values of x in question


    def create_graph(self, x):
        # plot log of error against L
        plt.rc('font', size = 32)
        plt.grid(linestyle = '--', linewidth = 0.5)

        L_vector = np.arange(0, 15, 1)
        # Can't have L too large or error with x**k at some 
        # point - 'int too large to convert to float'
        approximant_vector = []
        for i in range(len(L_vector)):
            approximant_vector.append(
                            diagonal_approximant(i, x))
        approximant_vector = np.array(approximant_vector)
        error_vector = f_1(x) - approximant_vector
        print(error_vector)
        log_error = np.log(np.absolute(error_vector))
        plt.plot(L_vector, log_error, color = 'C3')

        plt.xlabel('$L$')
        plt.ylabel('$\ln(Error)$')
        plt.tight_layout()
        plt.show()
        # Also plot something to do with error


    def display_graphs(self):
        self.create_graph(self.chosen_val1)
        self.create_graph(self.chosen_val2)



if __name__ == '__main__':
    # plot_comparison(3, 50) # N, L

    pade_test = approximant_investigation(10, 100)
    pade_test.display_graphs()

    