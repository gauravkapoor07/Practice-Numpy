#np.insert(array, index, value, axis=None)
import numpy as np
arr = np.array([10,20,30,40,50])
new_arr = np.insert(arr, 2, 100)
print(arr)
print(new_arr)  # Output: [ 10  20 100  30  40  50]

#2d
arr_2d = np.array ([[1,2,3],
                    [7,8,9]])
new_arr_2d = np.insert(arr_2d, 1, [4,5,6], axis=0)  # Insert a new row at index 1
print(arr_2d)

print(new_arr_2d)  # Output: [[1 2 3]
                   #          [4 5 6]
                   #          [7 8 9]]