#Mathematical Operations using NumPy

import numpy as np

arr = np.array([1,2,3,4,5,6])
#Aggregate functions to perform operations on the array
arr_sum = np.sum(arr)# Summing all elements
arr_mean = np.mean(arr)# Calculating the mean of elements
arr_min = np.min(arr)# Minimum value in the array
arr_std = np.std(arr)# Standard deviation of the array
arr_var = np.var(arr)# Variance of the array
print(f'Sum: {arr_sum}, Mean: {arr_mean}, Min: {arr_min}, Std: {arr_std}, Var: {arr_var}')
print(f'Sum: {arr_sum}, Mean: {arr_mean}')

#Mathematical operations like addition, subtraction, multiplication, and division
print(arr + 2)# Adding 2 to each element
print(arr * 2)# Multiplying each element by 2
print(arr - 2)# Subtracting 2 from each element
print(arr / 2)# Dividing each element by 2