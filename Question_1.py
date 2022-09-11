import numpy as np
import math
import matplotlib.pyplot as plt


def find_coefficient(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1/2
    numerator = (-1)**(k-1) * math.factorial(2*k - 3)
    denominator = 2**(2*k - 2) * math.factorial(k) * \
                        math.factorial(k-2)
    return numerator / denominator


def find_partial_sum(N):
    sum = 1  
    # c_0 = 1 and is always included in the sum 
    for i in range(1, N + 1):
        sum += find_coefficient(i)
    return sum


def plot_partial_sum(N):
    current_sum = 1
    y_vector = [1]
    for i in range(1, N + 1):
        current_sum += find_coefficient(i)
        y_vector.append(current_sum)

    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(y_vector, color = 'C0',  
        label = '$y = \sum_{k=0}^{N}c_{k}$')
    plt.axhline(math.sqrt(2), color = 'C1', 
        label = '$y = \sqrt{2}$')
    plt.legend(loc = 'best')
    plt.xlabel('$N$')
    plt.ylabel('$y$') 
    plt.show()


def error_bound(k):
    return 3 / (2*k)


def plot_error(N):
    current_sum = 1
    y_vector = [1]
    bound_vector = []
    for k in range(1, N + 1):
        current_sum += find_coefficient(k)
        y_vector.append(current_sum)
        bound_vector.append(error_bound(k))
    error_vector = np.array(y_vector) - math.sqrt(2)

    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(error_vector, color = 'C0')
    plt.plot(bound_vector, color = 'C1')
    plt.xlabel('$k$')
    plt.ylabel('$Error$') 
    plt.show()




if __name__ == '__main__':
    plot_error(10)
