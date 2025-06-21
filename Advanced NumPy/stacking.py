"""
vertically 
horizontally 

vstack() row wise
hstack() column wise

"""
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
# Vertical stacking
arr_vstack = np.vstack((arr1, arr2))
print(arr_vstack)
# Horizontal stacking
arr_hstack = np.hstack((arr1,arr2))
print(arr_hstack)