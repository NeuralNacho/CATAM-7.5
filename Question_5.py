import numpy as np
import math
import matplotlib.pyplot as plt
from Program_A import approximator
import Program_B


# Zeros will be from numerator and poles from denominator
# Care taken when these roots align

def find_poles(numerator_coefficients, 
    denominator_coefficients):
    poles_list = []
    denominator_roots = Program_B.find_roots\
                        (denominator_coefficients)
    numerator_roots = Program_B.find_roots\
                        (numerator_coefficients)
    checked_roots = set()  # will add the roots from numerator
    # checked already to this set

    for zero in denominator_roots:
        if zero in checked_roots:
            pass
        else:
            denominator_multiplicity = \
                (denominator_roots == zero).sum()
            numerator_multiplicity = \
                (numerator_roots == zero).sum()
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
    checked_roots = set() 

    for zero in numerator_roots:
        if zero in checked_roots:
            pass
        else:
            denominator_multiplicity = \
                (denominator_roots == zero).sum()
            numerator_multiplicity = \
                (numerator_roots == zero).sum()
            if numerator_multiplicity - \
                denominator_multiplicity > 0:
                zeros_list.append(zero)
            checked_roots.add(zero)

    return zeros_list


def find_f1_coefficient(k):
    if k == 0:
        return 1
    elif k == 1:
        return 1/2
    numerator = (-1)**(k-1) * math.factorial(2*k - 3)
    denominator = 2**(2*k - 2) * math.factorial(k) * \
                        math.factorial(k-2)
    return numerator / denominator


def find_f3_coefficient(k):
    if k == 0:
        return 1
    numerator = (-1)**(k) * math.factorial(2*k - 1)
    denominator = 2**(2*k - 1) * math.factorial(k) * \
                        math.factorial(k-1)
    return numerator / denominator


def find_f4_coefficient(k):
    return 1 / math.factorial(k)


def find_f5_coefficient(k):
    sum = 0
    for i in range(k + 1):
        sum += (-1)**(k-i) / math.factorial(i)
    return sum


def find_f6_coefficient(k):
    sum = 0
    for r in range(1 + math.floor(k / 2)):
        sum += math.comb(k-r, r) * find_f1_coefficient(k - r)
    return sum


def plot_results(results):
    plt.rc('font', size = 22)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.tight_layout()
    L = 1
    for result in results:
        # Use if statement for f6 graph:
        if L % 3 != 1:
            L += 1
            continue
        x = [element.real for element in result]
        y = [element.imag for element in result]
        plt.scatter(x, y, s = 60, 
            label = 'L = ${}$'.format(L))
        L += 1
    plt.legend(loc = 'upper right', prop={'size': 16},
                ncol = 2)
    plt.show()


def investigate_function(find_coefficient):
    # passing function find_coefficient as an argument
    # depending on function number
    poles_list = []
    zeros_list = []
    for L in range(1, 15):
        c_vector = np.empty([0], dtype = np.double)
        for i in range(2*L+ 1):
            c_vector = np.append(c_vector, 
                    find_coefficient(i))
        approximant = approximator(c_vector, L, L)
        numerator_coefficients = \
            np.flip(approximant.p_vector)
        denominator_coefficients = np.append(
            np.flip(approximant.q_vector), [1])
        
        poles = find_poles(numerator_coefficients, 
                            denominator_coefficients)
        zeros = find_zeros(numerator_coefficients, 
                            denominator_coefficients)
        
        poles_list.append(poles)
        zeros_list.append(zeros)
        #print('L = ', L, 'poles: ', poles)
        #print('L = ', L, 'zeros: ', zeros)
        
    #plot_results(zeros_list)
    plot_results(poles_list)


def generate_f5_table():
    real_poles = []
    for L in range(1, 11):
        c_vector = np.empty([0], dtype = np.double)
        for i in range(2*L+ 1):
            c_vector = np.append(c_vector, 
                    find_f5_coefficient(i))
        approximant = approximator(c_vector, L, L)
        numerator_coefficients = \
            np.flip(approximant.p_vector)
        denominator_coefficients = np.append(
            np.flip(approximant.q_vector), [1])
        
        poles = find_poles(numerator_coefficients, 
                            denominator_coefficients)
        for element in poles:
            if element.imag == 0 and (element + 1) < 0.03:
                real_poles.append(element)
    print(real_poles)


if __name__ == '__main__':
    investigate_function(find_f6_coefficient)
    # For f6 change plot to include less values of L
    # by going into plot_results function

    #generate_f5_table()