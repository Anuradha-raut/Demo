import numpy
from numpy import*

arr=array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
#1.Shape of the array
shape=numpy.shape(arr)
print("The shape of the array is:",shape)

#2.Dimension of the array
dimension=numpy.ndim(arr)
print("The dimension of the given array is:",dimension)

#3.Element of the array
print("The elements of the array:\n",arr)

# Basic operations on array
#1.concatenate
arr1=array(
    [
        [1,2],
        [3,4]
    ]
)
arr2=array(
    [
        [5,6],
        [7,8]
    ]
)

# concatenate by row wise
rows=concatenate((arr1,arr2),axis=0)
print("concatenation by row wise:\n",rows)

# concatenate by column wise
cols=concatenate((arr1,arr2),axis=1)
print("Concatenation by column wise:\n",cols)

# to print specific row wise as well as col wise
row=arr1[1,1]
print("specific row wise:",row)

col=arr2[0,1]
print("specific col wise:",col)

#slicing
result=arr1[:2:]
print(result)