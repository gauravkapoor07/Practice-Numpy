#np.isinf(array) 10^1000
import numpy as np

arr = np.array([1,2,np.inf, 4,-np.inf, 6])
print(np.isinf(arr))
# This will return a boolean array indicating where the infinite values are
# Output: [False False  True False  True False]

# Replace infinite values with a specific number, e.g., 0
cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)
# This will replace positive infinity with 1000 and negative infinity with -1000

