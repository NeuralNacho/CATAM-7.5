import numpy as np
import math


class approximator:
    def __init__(self, c_vector, L, M, x = None):
        self.c_vector = c_vector
        self.L = L
        self.M = M
        self.x = x

        self.solve5()
        # Calling this function calls self.solve4()
    
    def solve4(self):
        # 4 refers to name of exquation in project 
        # description

        if self.M == 0:
            self.q_vector = []
            # Will be empty if M = 0
            return

        # This vector is multiplied by the matrix
        c_target = np.negative(self.c_vector[self.L + 1 : 
                                    self.L + self.M + 1])
        # This is the product of the vector and matrix

        rows = []

        for i in range(self.M):
            # indexing matrix rows
            row = np.flip(self.c_vector[0 : 1 + self.L + i])
            # up to c_L
            if len(row) >= self.M:
                row = row[:self.M]
            else:
                additional_zeros = np.zeros(self.M - \
                                            len(row))
                # fill rest of row with zeros if space
                # (matrix has width M)
                row = np.append(row, additional_zeros)
            rows.append(row)
        
        c_matrix = np.vstack(rows)
        print(c_matrix)
        print(np.linalg.det(c_matrix))

        q_vector = np.linalg.lstsq(c_matrix, c_target)[0]
        # Need 0 index of result from lstsq function

        # NOTE: q_vector starts from q_1 unlike p_vector
        # which starts from p_1
        self.q_vector = q_vector


    def solve5(self):
        self.solve4()
        # Need to get q_k's first to solve (5)

        p_vector = np.empty([0])
        for k in range(self.L + 1):
            sum = 0
            for s in range(1, 1 + min(k, self.M)):
                sum += self.q_vector[s - 1] * \
                    self.c_vector[k - s]
                # s - 1 since q_vector starts from q_1
            p_k = self.c_vector[k] + sum
            
            p_vector = np.append(p_vector, p_k)

        self.p_vector = p_vector


    def R_LM(self, x):
        
        numerator = 0
        for k in range(self.L + 1):
            numerator += self.p_vector[k] * x ** k
        
        denominator = 1
        for k in range(1, self.M + 1):
            denominator += self.q_vector[k - 1] * x ** k
        
        return numerator / denominator



    def evaluate_approximant(self, x_vector):
        vfunc = np.vectorize(self.R_LM)
        # vectorise function so that it can be applied to
        # a set x

        return(vfunc(x_vector))



if __name__ == '__main__':
    c_vector = np.empty([0], dtype = np.double)
    # Can then append the coefficients to this list

    c_vector = np.append(c_vector, [0, 1, 0, 1/3, 0, 2/15, 0, 17/315, 0])
    L = 3
    M = 4

    approximant = approximator(c_vector, L, M)

    # For testing:
    print('c_vector: ', c_vector)
    print('p_vector: ', approximant.p_vector)
    print('q_vector: ', approximant.q_vector)
    # Index 0 entry of q_k meaningless but want to keep
    # other indexing consistent
    print(approximant.evaluate_approximant([1, 2, 3]))
