'''
import pysnooper
import numpy as np

@pysnooper.snoop()
def multi_matmul(times):
    x = np.random.rand(2, 2)
    w = np.random.rand(2, 2)

    for i in range(times):
        x = np.matmul(x, w)
    return x
'''
def if_else_test(a, b):
    max = 0
    if(a>b):
        max = a
        print("max = ", max)
    else:
        max = b
        print("max = ", max)


#multi_matmul(3)
if_else_test(input(), input())