import numpy as np

a = np.array([
    [1,   2,  3, 0],
    [-1, -2, -2, 1],
    [6,   1, -4, 0]
    ])

b = np.array([
    [-6., -5., -4., -3.], 
    [-2., -1.,  0.,  1.],
    [ 2.,  3.,  4.,  5.]
    ])
c = np.logical_and.reduce(a, axis=0)
d = np.logical_and.reduce(b, axis=0)





# https://en.wikipedia.org/wiki/AND_gate