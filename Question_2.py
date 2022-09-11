import numpy as np
from Program_A import approximator
import Question_1


if __name__ == '__main__':
    L = 3
    x = 1

    c_vector = np.empty([0], dtype = np.double)
    for i in range(2*L + 1):
        c_vector = np.append(c_vector, 
            Question_1.find_coefficient(i))
    approximant = approximator(c_vector, L, L)
    
    print('R_L,L(1) = ', 
        approximant.evaluate_approximant(1))

ITERATIVE IMPROVEMENT ?