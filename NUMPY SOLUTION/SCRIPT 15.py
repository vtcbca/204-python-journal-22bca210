#write a Numpy program to create a new shape to an array without changing its data.

import numpy as np
arr = np.array([[1, 2],[3, 4],[5, 6]])
reshaped_arr = np.reshape(arr, (2,3))
print("Original array:\n", arr)
print("Reshaped array:\n", reshaped_arr)

