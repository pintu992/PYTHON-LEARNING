import numpy as np


arr= np.array([[1,2,3,4,5],[4,5,6,7,8]], np.int32)

print(arr.ndim)           # "ndim" rreturn the dimension of array
print(arr.dtype)          # "dtype" return the type off data stored in array
print(arr.shape)          # "shape" return the shape of array
print(arr.flat)           # "flat"  create a flat iterator
print(arr.size)           # "size"   return the size of arrray
print(arr.itemsize)       # "itemsize"  gives the size of each element stored in array
print(arr.T)              # "T"   return the transpose of array
print(arr.nbytes)         # "nbytes"  return the total Bytes used by elements
print(arr.base)           # "base"   Object from which array is derived