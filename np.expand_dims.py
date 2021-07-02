# Add np array dims example.

import numpy as np

# expand_dims(a, axis)就是在axis的那一個軸上把數據加上去，這個數據在axis這個軸的0位置。 
# 例如 原本为一维的2个数据，axis=0，则shape变为(1,2),axis=1则shape变为(2,1) 
# 例如 原本为 (2,3),axis=0，则shape变为(1,2,3),axis=1则shape变为(2,1,3)

a = np.array([
    [2, 3, 4], [2, 2, 1]
    ])

print(a.shape)
print("axis=0:", np.expand_dims(a, 0).shape)
print("axis=1:", np.expand_dims(a, 1).shape)

a1 = a[np.newaxis]

print("\na1:", a1.shape)

print("\naxis0_a:", np.expand_dims(a, 0))
print("a1: ", a1)

import sys
sys.exit()
b = np.array([1,2,3])

print(b.shape)
print("axis=0:", np.expand_dims(b, 0).shape)
print("axis=1:", np.expand_dims(b, 1).shape)
