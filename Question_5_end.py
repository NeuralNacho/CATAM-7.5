import numpy as np
import math
import matplotlib.pyplot as plt
from Program_A import approximator
import Program_B
import Question_5


def f_6(x):
    return math.sqrt(1 + x + x**2)


def R_LL(x, L):
    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L+ 1):
        c_vector = np.append(c_vector, 
                Question_5.find_f6_coefficient(i))
    approximant = approximator(c_vector, L, L)
    print(L, approximant.p_vector)
    print(L, approximant.q_vector)
    return approximant.evaluate_approximant(x)


def plot_graph1(L):
    x = np.linspace(-20, 7.5, 1000)

    y_approx_even = R_LL(x, 10)
    y_approx_odd = R_LL(x, 5)
    y_approx_odd_2 = R_LL(x, 17)
    y_actual = np.vectorize(f_6)(x)

    plt.rc('font', size = 28)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.plot(x, -y_actual, color = 'black', 
                label = '$y = -f_{1}(x)$')
    plt.plot(x, y_approx_odd, color = 'blue', 
                label = '$y = R_{5,5}(x)$')
    plt.plot(x, y_approx_even, color = 'red', 
                label = '$y = R_{10,10}(x)$')
    plt.plot(x, y_approx_odd_2, color = 'green', 
                label = '$y = R_{17,17}(x)$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.ylim(-20, 8)
    plt.tight_layout()
    plt.legend(loc = 'best')
    plt.show()



if __name__ == '__main__':
    plot_graph1(8)

