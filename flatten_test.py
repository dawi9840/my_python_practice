import numpy as np
a = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])

b  = a.flatten()     #按照 row 来降维
b1 = a.flatten('A')  #按照 row 来降维
c  = a.flatten('F')  #按照 column 来降维

print("a:", a)
print("flatten_a:", b)
print("flatten_a(A):", b1)
print("flatten_a(F):", c)

