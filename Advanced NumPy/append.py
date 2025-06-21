#np.append(array, values, axis=None)
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.append(arr, [60,70,100])
print(arr)  # Output: [10 20 30 40 50]
print(new_arr)  # Output: [10 20 30 40 50 60 70 100]

# 2d
arr_2d = np.array([[1, 2, 3],
                    [7, 8, 9]])
new_arr_2d = np.append(arr_2d, [[4, 5, 6]], axis=0)  # Append a new row
print(arr_2d)
print(new_arr_2d)  # Output: [[1 2 3]
                    #          [7 8 9]
                    #          [4 5 6]]