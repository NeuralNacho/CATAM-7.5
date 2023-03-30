import numpy as np
import math
import matplotlib.pyplot as plt
from Program_A import approximator
import Question_1


def tabulate_error(L):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 1):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    pade_approximants = []
    for m in range(L + 1):
        approximant = approximator(c_vector, m, m)
        pade_approximants.append(
            approximant.evaluate_approximant(1))
    
    error_vector = np.absolute(np.array(pade_approximants) \
                                    - math.sqrt(2))
    
    print('L        Error')
    for k in range(L + 1):
        print(k, '\t', error_vector[k])


def plot_log_error(L):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 1):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    pade_approximants = []
    for m in range(0, L + 1):
        approximant = approximator(c_vector, m, m)
        pade_approximants.append(
            approximant.evaluate_approximant(1))
    error_vector = np.absolute(np.array(pade_approximants) \
                                    - math.sqrt(2))
                
    log_vector = np.log(error_vector)
    x_vector = np.arange(len(log_vector))

    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(log_vector, color = 'C2')
    plt.xlabel('$L$')
    plt.ylabel('$\ln(Error)$') 
    plt.xticks(x_vector)
    plt.show()


if __name__ == '__main__':
    L = 15
    x = 1

    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 1):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    approximant = approximator(c_vector, L, L)
    estimate = approximant.evaluate_approximant(1)
    
    tabulate_error(L)
    # print('Machine precision: ', np.finfo(np.float64).eps)
    #plot_log_error(10)

# ITERATIVE IMPROVEMENT ?