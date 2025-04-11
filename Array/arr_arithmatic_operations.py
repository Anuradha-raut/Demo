import numpy
from numpy import*

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
#1.Addition
add=arr1+arr2
print("addition of two arrays:\n",add)

#2.Subtraction
sub=arr1-arr2
print("subtraction of two arrays:\n",sub)

#3.multiplication
mul=arr1*arr2
print("Multiplication of two arrays:\n",mul)

#4.Division
div=arr1/arr2
print("Division of two arrays:\n",div)

#5.Modulus
mod=arr2%arr1
print("modulus of two arrays:\n",mod)

# Some aggregate functions
#1.sum
sum1=sum(arr1)
print("Sum of array 1 is:",sum1)

sum2=sum(arr2)
print("Sum of array 2 is:",sum2)

#2.Mean
mean1=mean(arr1)
print("The mean of array 1 is:",mean1)

mean2=mean(arr2)
print("The mean of array 2 is:",mean2)

#3.median
median1=median(arr1)
print("The median of array 1 is:",median1)

median2=median(arr2)
print("The median of array 2 is:",median2)
