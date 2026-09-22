import numpy as np



array1 = np.random.rand(2,2)  #"random.rand" creats an array filled with random values in interval (0,1) of given size
print(array1)

array2= np.random.randn(2,2)  #"random.randn" creats an array filled with random values
print(array2)

array3= np.random.randint(1,10 ,size=(2,3)) #"random.randint" creats a array filled with random integers in given range of given size
print(array3)