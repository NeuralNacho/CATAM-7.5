import numpy as np
import math
import matplotlib.pyplot as plt
from Program_A import approximator


def asymptotic_series(order, x):
    # order is the highest power of x
    sum = 0
    for i in range(order + 1):
        sum += (-1)**i * math.factorial(i) * x**i
    return sum


def find_expansion_coefficient(k):
    return (-1)**k * math.factorial(k)


def generate_approximant(L, M):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(L + M + 1):
        c_vector = np.append(c_vector, 
                find_expansion_coefficient(i))
    approximant = approximator(c_vector, L, M)
    return approximant


def get_error(series_order, L, M):
    x_vector = np.append( np.arange(1, 10) / 10, 
                        np.arange(1, 21) )
    numerical_results = [0.91563334, 0.85211088, 
0.80118628, 0.75881459, 0.72265723, 0.69122594, 0.66351027,
0.63879110, 0.61653779, 0.59634736, 0.46145532, 0.38560201,
0.33522136, 0.29866975, 0.27063301, 0.24828135, 0.22994778,
0.21457710, 0.20146425, 0.19011779, 0.18018332, 0.17139800,
0.16356229, 0.15652164, 0.15015426, 0.14436271, 0.13906806,
0.13420555, 0.12972152]

    series_results = np.empty([0])
    for i in range(len(x_vector)):
        series_results = np.append(series_results, 
                asymptotic_series(series_order, x_vector[i]))
    
    approximant = generate_approximant(L, M)
    approximant_results = \
        approximant.evaluate_approximant(x_vector)
    
    series_error = np.absolute(series_results - 
                                    numerical_results)
    approximant_error = np.absolute(approximant_results - 
                                    numerical_results)
    return series_error, approximant_error
                    

def plot_series_error(y):
    # Plots the error given x
    x_vector = np.arange(1, 11) / 10
    plt.rc('font', size = 20)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(x_vector, np.log(y[:10]), color = 'C2')
    plt.xlabel('$x$')
    plt.ylabel('$\ln(Error)$')
    plt.tight_layout()
    x_ticks = np.arange(0, 1.2, 0.2)
    plt.xticks(x_ticks)
    plt.show()


def plot_approximant_error(y):
    # Plots the error given x
    #x_vector = np.append( np.arange(1, 10) / 10, 
    #                    np.arange(1, 21) )
    x_vector = np.arange(1, 11) / 10
    # switch x_vector depending on graph desired
    plt.rc('font', size = 20)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(x_vector, np.log(y[:len(x_vector)]), color = 'C0')
    # plt.plot(x_vector, y[:len(x_vector)], color = 'C0')
    # plot without log for [0, 20] range
    plt.xlabel('$x$')
    plt.ylabel('$\ln(Error)$')
    plt.tight_layout()
    # x_ticks = np.append([0, 0.5], np.arange(1, 21))
    # x_ticks = list(range(0, 21, 2))
    x_ticks = np.arange(0, 1.2, 0.2)
    plt.xticks(x_ticks)
    plt.show()


def get_series_error_change(x, actual_value, order_vector):
    series_error = np.empty([0])
    for N in range(len(order_vector)):
        series_error = np.append( series_error, 
                abs(asymptotic_series(N + 1, x) - 
                                        actual_value) )
    return series_error


def get_approximant_error_change(x, actual_value, L_vector):
    approximant_error = np.empty([0])
    for L in range(len(L_vector)):
        approximant = generate_approximant(L + 1, L + 1)
        approximant_result = approximant.\
            evaluate_approximant(x)
        approximant_error = np.append( approximant_error, 
            abs(approximant_result - actual_value) )
    return approximant_error


def plot_series_error_change():
    # Plots the error from power series varying order
    order_vector = np.arange(1, 13, 1)
    x_list = [0.1, 1, 20]
    numerical_results = [0.91563334, 0.59634736, 0.12972152]
    for index in range(len(x_list)):
        plt.rc('font', size = 32)
        plt.grid(linestyle = '--', linewidth = 0.5)
        y = get_series_error_change(x_list[index], 
                                numerical_results[index], 
                                order_vector)
        plt.plot(order_vector, np.log(y), color = 'C3')
        plt.ylabel('ln(Error) for ' '$x = {}$'.\
                        format(x_list[index]))
        plt.xlabel('$Order$')
        plt.tight_layout()
        plt.xticks(order_vector)
        plt.show()

    
def plot_approximant_error_change():
    L_vector = np.arange(1, 13, 1)
    # Plots the error varying L or order
    x_list = [0.1, 1, 20]
    numerical_results = [0.91563334, 0.59634736, 0.12972152]
    for index in range(len(x_list)):
        plt.grid(linestyle = '--', linewidth = 0.5)
        y = get_approximant_error_change(x_list[index], 
                                numerical_results[index],
                                L_vector)
        plt.rc('font', size = 12)
        plt.plot(L_vector, np.log(y))
        plt.xlabel('$L$')
        plt.ylabel('ln(Error) for ' '$x = {}$'.\
                        format(x_list[index]))
        plt.tight_layout()
        plt.xticks(L_vector)
        plt.show()


if __name__ == '__main__':
    #plot_series_error_change()
    #plot_approximant_error_change()

    series_error, approximant_error = get_error(1, 7, 7)
    # change order from 1 to 9
    #plot_series_error(series_error)
    plot_approximant_error(approximant_error)
