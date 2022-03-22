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
print(np.arange(2))
print("====")
#reshape- usd to change the shape of an existing array
#the new array to be created must have the same no of  elements as the original array
zz= np.array([20,21,22,23,24,25])
print(zz)
zz2= zz.reshape(3,2)
print(zz2)

#reshape can also perform the opposite...
#convert a multidmensional array into a single dimensional array

zz3=zz2.reshape(6)
print(zz3)
#we can also use flatten() method to achieve the same results...
zz4=zz2.flatten()
print(zz4)


#indexing and slicing
aa=np.arange(1,10)
print(aa[0:2])
print(aa[5:])
print(aa[:2])
print(aa[-3:])

#conditions
#we can provide conditions to be satisfied for items to be printed
xx=np.arange(1,10)
print(xx[xx<4])
#we can  combine two conditions using &
print(xx[(xx<4) & (xx%2==0)])
#we can also assign the condition to a variable
y=(xx<6) &(xx%2==0)
print(xx[y])'''
#operations
x=np.arange(1,10)
print(x.sum())#sum of elements
print(x.min()) #find the min
print(x.max()) #find the max
y=x*2#multiply everything by 2
print(y)







