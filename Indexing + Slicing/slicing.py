#array[start:stop:step] 1d
#arr[start:end] start to end-1
#array[start_row:stop_row, start_column:stop_column] 2d
import numpy as np

arr = np.array([10,20,30,40])

arr_slice = arr[1:3]  # Slicing from index 1 to 3 (4 is exclusive)
arr_slice1 = arr[:4] # Slicing from the start to index 3 (4 is exclusive)
arr_slice2 = arr[::2] # Slicing with a step of 2
arr_slice3 = arr[::-1]  # Reverse the array
print(arr_slice)  # Output: [2 3 4]
print(arr_slice1)  # Output: [1 2 3 4]
print(arr_slice2)  # Output: [1 3 5]
print(arr_slice3) # Output: [5 4 3 2 1]
