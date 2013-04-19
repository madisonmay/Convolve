from random import randint
from numpy import np

def random_kernel(n, max, value)
    kernel = np.zeros(n, n)
    for i in range(size):
        for j in range(size):
            kernel[i][j] = randint(-max, max)
    kernel[n/2][n/2] = -np.sum(kernel)

