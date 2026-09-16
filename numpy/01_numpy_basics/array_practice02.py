#Check Whether a Numpy Array contains a Specified Row

import numpy as np

arr= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row = [4, 5, 6]

if any(np.array_equal(row, r) for r in arr):
    print("Row exists in the array.")

print(row in arr.tolist())