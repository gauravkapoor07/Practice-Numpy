#Problem
list1 = [1,2,3]
list2 = [4,5,6]

result_prob = [x+y for x,y in zip(list1, list2)]
print(result_prob)
#it is slower than numpy vectorization
# The above code uses a list comprehension to add two lists element-wise.
# However, it is not as efficient as using NumPy for vectorized operations.

#Solution
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result_sol = arr1 + arr2
print(result_sol)   