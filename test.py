import numpy as np
arr = np.arange(20).reshape(4,5)
arr1=arr[2, arr.sum(axis = 0)>30]
print(arr1)

a = np.array([97,101,105,111,117,125])
b = np.array(['a','e','i','o','u','y'])

def filter(a,b):
    c = np.where((a>100) &(a<110))
    return b[c]



mylist = [0,4,1,2,0,4]
c = np.array(mylist)
d = c.reshape(2,3)
print(d)

def max_and_min(matrix):
    for i in range(len(matrix)):
        x = np.amax(matrix, axis=1)
        y = np.amin(matrix, axis =1) 
        print(f"maksymalna wartość w wierszu {i} to {x[i]}, minimalna wartość w wierszu {i} to {y[i]},")
    
e = np.arange(11)    
for i in e:
    if ((i>3) & (i < 8)):
        e[i] = -i
    print(e)
