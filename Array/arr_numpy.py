import numpy
from numpy import*

# By using array()
# integer
arr=array([2,3,4,6],dtype=int)
for i in arr:
    print(i)

# string
arr=array(["pune","nashik","kolhapur"],dtype=str)
for i in arr:
    print(i)

# copy one array to other array
arr1=array([9,8,7,6],dtype=int)
arr2=array(arr1)
for i in arr2:
    print(i)

# By using linspace()
arr=linspace(0,10,6)
for i in arr:
    print(i,end=" ")

# By using logspace()
arr=logspace(1,5,6)
for i in arr:
    print(i)

# By using arange()
#arr=arange(1,11,1)
arr2=arange(10,0,-1)
for i in arr2:
    print(i)

# By using
arr = zeros(5, int)
for i in arr:
    print(i,end=" ")