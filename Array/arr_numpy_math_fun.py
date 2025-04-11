# mathematical functions using numpy in array
import numpy
from numpy import*

# sin():
arr1=array([1,2,3,4,5])
result=numpy.sin(arr1)
print("sin of array:",result)

# cos()
arr1=array([2,3,4,5])
result=numpy.cos(arr1)
print("cos of array:",result)

# sqrt()
arr1=array([4,9,16,25])
result=numpy.sqrt(arr1)
print("Square root of array is:",result)

# abs()
arr1=array([1,2,3,4])
result=abs(arr1)
print("Absolute value of array is:",result)

# maximum and minimum of array
arr1=array([10,20,30,40,50])
result1=max(arr1)
result2=min(arr1)
print("Maximum number from given array:",result1)
print("Minimum number from given array",result2)

# sum()
arr1=array([1,2,3,4])
sum=arr1+2
print("Sum is:",sum)

# mean()
arr1=array([10,20,30,40,50])
result=numpy.mean(arr1)
print("mean of the array is:",result)