#np.delete(array, index, axis=None)

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.delete(arr, 2)  # Delete the element at index 2
print(new_arr)  # Output: [10 20 40 50 60]  

#2d
arr_2d = np.array([[1, 2, 3],
                    [7, 8, 9]]) 
new_arr_2d = np.delete(arr_2d, 1, axis=0)  # Delete the row at index 1
print(arr_2d)
print(new_arr_2d)  # Output: [[1 2 3]]