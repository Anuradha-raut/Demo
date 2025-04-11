# mathematical operations on array
from numpy import*

# Addition
arr1=array([1,2,3,4,5])
arr2=array([5,4,3,2,1])
arr3=arr1 + arr2
print("Addition of two arrays:",arr3)

# Subtraction
arr1=array([1,2,3,4])
arr2=array([5,7,4,8])
arr3=arr2-arr1
print("Subtraction of two arrays is:",arr3)

# Multiplication
arr1=array([1,2,3,4,5])
arr2=arr1*5
print("After multiply the given array by '5':",arr2)

# Division
arr1=array([10,20,30,40])
arr2=arr1/2
print("After dividing the given array by '3:",arr2)

arr1=array([10,20,30])
arr2=array([2,5,10])
arr3=arr1/arr2
print("division of array:",arr3)