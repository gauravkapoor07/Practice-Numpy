import numpy as np

arr = np.array([1.2,1.3,2.5])
print(arr.dtype)#FLOAT64
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)#INT64