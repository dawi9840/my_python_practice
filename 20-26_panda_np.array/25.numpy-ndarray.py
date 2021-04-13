import numpy as np

#建立一維陣列
'''
data = np.array([3, 2, 6, 10])
data1 = np.empty(4)            #創一有4個資料的一維陣列，資料未指定
data2 = np.zeros(3)
data3 = np.ones(3)
data4 = np.arange(5)

print("data: ", data)
print("data1:", data1) 
print("data2:", data2)
print("data3:", data3)
print("data4:", data4)
'''
#建立二維陣列
'''
data = np.array([ [1, 2, 3], [2, 1, 2], [3, 6, 9] ]) #3x3的2維陣列
data1 = np.empty([3, 3])
data2 = np.ones([2, 3])

print("data=", data)
print("data1:", data1) 
print("data2:", data2)
'''
#建立三維陣列
'''
data = np.array([ 
    [
        [1, 2, 4], [3, 1, 4]
    ],
    [
        [2, 3, 4], [7, 8, 4]
    ]
]) #2x2x2的3維陣列

print("shap=", data.shape)
print("ndim=", data.ndim)


data1 = np.zeros([3, 1, 3])
print("data1:", data1) 
'''
#建立高維陣列
'''
data = np.array([
    [
        [
            [1, 2, 3], [3, 6, 9]
        ]
    ]
])   #1x1x2x3的四維陣列 '''
data1 = np.ones([2, 1, 1, 2])
print("data1=", data1)