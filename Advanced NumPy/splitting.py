"""

np.split(array ,indices_or_sections, axis=0 or 1)
np.hsplit() Horizontal split
np.vsplit() Vertical split

"""

import numpy as np
# Create a sample array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Split the array into 3 equal parts along the first axis (rows)
split_arr = np.split(arr, 3, axis=0)
print(split_arr)
# Output: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]])]
# Split the array into 2 equal parts along the second axis (columns)
split_arr_col = np.split(arr, 2, axis=1)
print(split_arr_col)
# Output: [array([[1, 2], [5, 6], [9, 10]]), array([[ 3,  4], [ 7,  8], [11, 12]])]
# Horizontal split
h_split_arr = np.hsplit(arr, 2)
print(h_split_arr)
# Output: [array([[1, 2], [5, 6], [9, 10]]), array([[ 3,  4], [ 7,  8], [11, 12]])]
# Vertical split
v_split_arr = np.vsplit(arr, 3)
print(v_split_arr)
# Output: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]])]

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

arr_split = np.split(arr1, 5)
print(arr_split)