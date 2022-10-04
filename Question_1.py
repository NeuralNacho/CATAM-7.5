import numpy as np
import math
import matplotlib.pyplot as plt


def odd_product(last_int):
    product = 1
    next_int = 1
    while next_int <= last_int:
        product *= next_int
        next_int += 2
    return product


def find_coefficient(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1/2
    numerator = (-1)**(k-1) * math.factorial(2*k - 3)
    denominator = 2**(2*k - 2) * math.factorial(k) * \
                        math.factorial(k-2)
    return numerator / denominator

    # numerator = (-1)**(k-1) * odd_product(2*k - 3)
    # denominator = 2**k * math.factorial(k)
    # return numerator / denominator




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


def error_bound(N):
    return 0.69 * 1/math.sqrt(2*N) * 1/(2*N + 2)
    return 0.69 * 2**(-2*N) * (math.factorial(2*N - 1)) / \
        (math.factorial(N - 1) * math.factorial(N + 1))


def plot_error(N):
    current_sum = 1
    y_vector = []
    bound_vector = []
    x_axis = np.arange(1, N + 1, 1)
    for m in range(1, N + 1):
        current_sum += find_coefficient(m)
        y_vector.append(current_sum)
        bound_vector.append(error_bound(m))
    error_vector = np.array(y_vector) - math.sqrt(2)

    plt.rc('font', size = 32)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(x_axis, error_vector, color = 'C0', 
                        label = '$Actual$ $error$')
    plt.plot(x_axis, bound_vector, color = 'C1', 
                        label = '$Error$ $bound$')
    plt.plot(x_axis, np.negative(bound_vector), color = 'C1')
    plt.legend(loc = 'best')
    plt.xticks(np.append(0, x_axis))
    plt.xlabel('$N$')
    plt.ylabel('$Error$') 
    plt.show()


def tabulate_error(N):
    partial_sums = []
    current_sum = 0
    for m in range(N + 1):
        current_sum += find_coefficient(m)
        partial_sums.append(current_sum)
    
    error_vector = np.absolute(np.array(partial_sums) \
                                    - math.sqrt(2))
    
    print('N        Error')
    for k in range(N + 1):
        print(k, '\t', error_vector[k])


def find_xi(N):
    power = 1/2 - N
    partial_sum = find_partial_sum(N)
    error = abs(math.sqrt(2) - partial_sum)
    coefficient = 2**(-2*N) * (math.factorial(2*N - 1)) / \
        (math.factorial(N - 1) * math.factorial(N + 1))
    xi = (error / coefficient)**(1 / power) - 1
    return xi


def print_xi_factor(N):
    for i in range(1, N + 1):
        print( (1+find_xi(i))**(1/2 - i))


if __name__ == '__main__':
    tabulate_error(11)
    #plot_error(10)
    #print( find_xi(50) )
    #print_xi_factor(90)
