# Concat operator
from array import*

arr=array('i',[])
arr2=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in array is:")
print(arr)

how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr2.append(int(input("Enter the elements:")))
print("After adding elements in array 2 is:")
print(arr2)

# After using concatenation operator in array
result=arr+arr2
for i in result:
    print(i, end=" ")

