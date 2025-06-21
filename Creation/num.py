import numpy as np

Temperature = np.array([0,1,2,3,4,5,6])
average = np.mean(Temperature)
print(f'(The Temperature are: ', Temperature, ' and the average is: ', average, ')')
# Output: (The Temperature are:  [0 1 2 3 4 5 6] and the average is:  3.0 )


# 2-D Array
arr_2d = np.array([[1,2,3],
                  [4,5,6], 
                  [7,8,9]])
print(arr_2d)