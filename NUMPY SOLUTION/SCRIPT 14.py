#write a numpy program to get the values and indices of the elements that are bigger than 10 in a given array.

import numpy as np
arr = np.array([1, 11, 2, 12, 3, 13])
indices = np.where(arr > 10)
values = arr[indices]
print("Indeces of elements grater than 10:",indices)
