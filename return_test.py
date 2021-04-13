def a_function(a, b):
    return a+b

def b_function(a, b):
    a+b
    #print("a+b:", a+b)


#print("a_function value:", a_function(1,2))
#print("b_function value:", b_function(1,2))

'''
memberdata = input('輸入帳號/姓名(按enter結束):')
memberdata = memberdata + "/x"
split_input = memberdata.split("/", 1)
print(memberdata)
print(split_input)'''

'''import numpy as np
a = np.linspace(1, 10, 3)
print(a)'''


import numpy as np
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabel('some numbers')

plt.show()