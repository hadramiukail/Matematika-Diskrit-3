import numpy as np
nodes = ['P','Q','R','S','T']
A = np.array([
    [0, 5, 2, 0, 0],
    [5, 0, 0, 1, 0],
    [2, 0, 0, 3, 4],
    [0, 1, 3, 0, 6],
    [0, 0, 4, 6, 0]
])
print(A)

degree = np.sum(A > 0, axis=1)
print(degree)