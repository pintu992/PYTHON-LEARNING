"""NumPy supports several numerical data types, including:

Boolean: Represented by numpy.bool_, it stores True or False values.

Integer: Includes various bit-widths like numpy.int8, numpy.int16, numpy.int32, and numpy.int64.

Unsigned Integer: Similar to integers but without a sign, such as numpy.uint8, numpy.uint16, numpy.uint32, and numpy.uint64.

Floating Point: Includes numpy.float16, numpy.float32, and numpy.float64.

Complex: Represented by numpy.complex64 and numpy.complex128, these store complex numbers with real and imaginary parts."""

import numpy as np
# Create an array of strings
arr = np.array(["hello", "world"])
print(arr)
print(arr.dtype)

# Create an array of integers
arr2 = np.array([1, 2, 3, 4], dtype=np.int32)
print(arr2)
print(arr2.dtype)

#taking float data type
result = np.power(10, 2, dtype=np.float64)
print(result)