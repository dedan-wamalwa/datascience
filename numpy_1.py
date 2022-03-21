# numpy tutorial
import numpy as np
# creating an array in numpy
# an array in numpy is homogenous
'''x=np.array([1,2,3,4])
print(x[0])
# multidimensional arrays
x2=np.array([[1,2,3],[5,6,7],[8,9,10],[11,12,13]])
print(x2)
print(x2[0][2])
# array methods
print("===methods===")
print(x2.ndim) #no of dimensions of the array
print(x2.size) #total no. of items stored in the array
print(x2.shape) #tuple showing the no. of elements stored in each dimension of the array
print("=====")
print(np.append(x,17)) #appending items to the array
print(np.delete(x,1))
print(np.arange(2))'''
print("====")
#reshape- usd to change the shape of an existing array
#the new array to be created must have the same no of  elements as the original array
zz= np.array([20,21,22,23,24,25])
print(zz)
zz2= zz.reshape(3,2)
print(zz2)
