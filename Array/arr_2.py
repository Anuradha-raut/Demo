from array import*

# Add elements in array using insert method:
# by using index number
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert: "))
for i in range(0,how_many_elements):
   arr.append(int(input("Enter the elements:")))
print("After adding elements in array is:")
print(arr)
indx=int(input("Enter the index number:"))
value=int(input("Enter the value:"))
for i in arr:
    arr.insert(indx,value)
    print(i,end=" ")

# index number
arr2=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr2.append(int(input("Enter the elements:")))
print("After adding elements in array2 is:")
print(arr2)
arr2[2]=100
for i in arr2:
    print(i,end=" ")'''

# Using append method
arr1=array('i',[1,2,3,4,5])
arr1.append(6)
for i in arr1:
    print(i,end=" ")

