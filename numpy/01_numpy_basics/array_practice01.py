#Find number of occurrences of a sequence
import numpy as np

arr = np.array([[2, 8, 9, 4],
                [9, 4, 9, 4],
                [4, 5, 9, 7],
                [2, 9, 4, 3]])
count = 0
seq = np.array([9, 4])
for seq in arr.tolist():
    count+=1
print(count)
