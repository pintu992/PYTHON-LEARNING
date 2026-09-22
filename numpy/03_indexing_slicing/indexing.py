import numpy as np 
array = np.arange(1,10,2)
print(array)
print(array[3])  # acccesing element at index 3

array2= np.eye(3,3)
print(array2[2,2])   # accesing elelemnt in 2-D array

cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[1,2,0])  #accesing element in a 3-D array