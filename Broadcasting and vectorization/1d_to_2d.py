import numpy as np

arr1 = np.array([[1,2,3], [4,5,6]]) #2d matrix of (2,3)
arr2 = np.array([10,20,30]) # MATCHING DIMENSIONS

result = arr1 + arr2
print(result)
# PROBLEM OF IMCOMPATIBLE DIMENSIONS/SHAPES
arr3 = np.array([10,20]) # NOT MATCHING DIMENSIONS
result1 = arr1 + arr3
print(arr3)
# This will raise an error because the dimensions do not match for broadcasting