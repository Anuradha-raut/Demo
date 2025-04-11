# Attributes of array
from numpy import*

arr1=array([[5,6,7,8],[2,4,5,8]])
arr2=array([1,7,9,23])

# ndim(): The ndim attribute return the dimension of array.
print("The ndim of arr1=",ndim(arr1))
print("The ndim of arr2=",ndim(arr2))

# size() : The size() method, return total number of element present in array.
print("The size of arr1=",size(arr1))
print("The size of arr2=",size(arr2))

# shape() : This method return how many rows and cols present in array.
print("The shape of arr1:",shape(arr1))
print("The shape of arr2:",shape(arr2))

# dtype : This method allocate the data type to array. by default array has dtype=None.
print("dtype of arr1:",dtype(int))

#itemsize() : This method returns total memory size of element in bytes.
print("item size of arr1:",arr1.itemsize)
print("item size of arr2:",arr2.itemsize)

# reshape() : This method change the shape of array.
print("reshape of the arr1:",arr1.reshape(4,2))
print("reshape of the arr2:",arr2.reshape(2,2))

#nbytes() : This attribute return total memory occupied by array. 1 element is of 8bytes ---> 1-bit
print("n bytes of arr1:",arr1.nbytes)
print("n bytes of arr2:",arr2.nbytes)