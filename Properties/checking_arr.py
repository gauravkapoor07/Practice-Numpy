#checking shape of the matrix

import numpy as np

arr_2d = np.array([[1,2,3],
                   [4,5,6]])
arr_2d_shape = arr_2d.shape #SHAPE
print(arr_2d_shape)

arr_2d_size = arr_2d.size #SIZE
print(arr_2d_size)

arr_2d_ndim = arr_2d.ndim #DIMENSION
print(arr_2d_ndim)

arr_2d_dtype = arr_2d.dtype #DATA TYPE
print(arr_2d_dtype)
