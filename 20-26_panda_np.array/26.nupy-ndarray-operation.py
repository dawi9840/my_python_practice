import numpy as np

#逐元運算(elementwice)，2個data的shape必須一樣
d1 = np.array([3, 2 ,10])
d2 = np.array([1, 3, 6])
'''
print("addition:", d1+d2)
print("multiplication:", d1*d2)
print("d1 > d2:", d1>d2)
print("d1 == d2:", d1==d2)
'''
#矩陣運算(matrix)
da1 = np.array([
    [1, 3]
])#1x2
da2 = np.array([
    [2, -1, 3],
    [-2, 4, 1]
])#2x3
'''
print("Inner product:", da1.dot(da2))       #1x3
print("Outer product:", np.outer(da1, da2)) #2x6: (1x2)x(2x3)
'''
#統計運算(statistic)
#ndarray 多維陣列
data1 = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])#2x3
'''
print("ndarray summation:", data1.sum())
print("max:", data1.max() )
print("min:", data1.min() )
print("mean:", data1.mean())

print("Standard Deviation:", data1.std())
'''
print("data1:", data1)
print("sum of the column(axis=0):", data1.sum(axis=0)) 
print("sum of the row   (axis=1):", data1.sum(axis=1))
'''
print("max of the cloumn:", data1.max(axis=0))
print("max of the row:", data1.max(axis=1))
print("mean of the row:", data1.mean(axis=1))

print("cumulative sum :", data1.cumsum())
print("cumulative sum of the column:", data1.cumsum(axis=0)) #針對第1個維度做逐值累加
print("cumulative sum of the row:", data1.cumsum(axis=1))
'''