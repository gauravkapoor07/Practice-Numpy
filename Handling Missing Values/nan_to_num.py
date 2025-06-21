# np.nan_to_num(arr, nan=value) default = 0

# np.nan_to_num(array, copy=True, nan=0.0)
# np.nan_to_num(array, copy=False, nan=0.0)
import numpy as np

arr = np.array([1,2,np.nan, 4,np.nan, 6])

cleaned_arr = np.nan_to_num(arr) # Converts NaN to 0 by default
# You can also specify other values for NaN, positive infinity, and negative infinity
print(cleaned_arr)

cleaned_arr_custom_num = np.nan_to_num(arr, nan=5)
print(cleaned_arr_custom_num)