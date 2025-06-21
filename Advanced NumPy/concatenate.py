#np.concatenate((array1, array2), axis=0)
#axis 0 > vertical stacking
#axis 1 > Horizontal stacking
import numpy as np
# Concatenate 1D arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
arr3 = np.concatenate((arr1, arr2))
print(arr3)  # Output: [10 20 30 40 50 60]
# Concatenate 2D arrays vertically
arr2d_1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
arr2d_2 = np.array([[7, 8, 9],
                    [10, 11, 12]])
arr2d_concat = np.concatenate((arr2d_1, arr2d_2), axis=0)
print(arr2d_concat)
# Output: [[ 1  2  3]
#          [ 4  5  6]
#          [ 7  8  9]
#          [10 11 12]]
# Concatenate 2D arrays horizontally
arr2d_h1 = np.array([[1, 2],
                      [3, 4]])
arr2d_h2 = np.array([[5, 6],
                      [7, 8]])
arr2d_h_concat = np.concatenate((arr2d_h1, arr2d_h2), axis=1)
print(arr2d_h_concat)
# Output: [[1 2 5 6]
#          [3 4 7 8]]
# Concatenate 1D and 2D arrays
arr1_1d = np.array([10, 20, 30])
arr2d_1_2d = np.array([[1, 2, 3],
                        [4, 5, 6]])
arr1_2d_concat = np.concatenate((arr1_1d.reshape(1, -1), arr2d_1_2d), axis=0)
print(arr1_2d_concat)
# Output: [[10 20 30]
#          [ 1  2  3]
#          [ 4  5  6]]

