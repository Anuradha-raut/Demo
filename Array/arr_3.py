from array import*

# 1.copy method
''' arr=array('i',[])
arr2=[]
how_many_elements=int(input("Enter how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in the array the array looks like:")
for i in arr:
    print(i, end=" ")
# copy first array in second
print("\nThe second array is:")
arr2=arr.__copy__()
for i in arr2:
    print(i,end=" ")'''

# 2.pop method
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("The given array is:",arr)

arr.pop()
for i in arr:
    print(i,end=" ")'''

# remove method
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("The given array is:",arr)

result=arr.remove(2)
for i in arr:
    print(i,end=" ")'''

# reverse method
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert in array:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in array:")
print(arr)

result=arr.reverse()
for i in arr:
    print(i,end=" ")'''

# sort method
'''arr=array('i',[])
arr2=[]
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in array:",arr)

sorted(arr)
for i in arr:
    print(i,end=" ")'''

# extend method
'''arr1=array('i',[])
arr2=array('i',[4,5])
how_many_elements=int(input("Enter the how many elements you want to insert in array:"))
for i in range(0,how_many_elements):
    arr1.append(int(input("Enter the elements:")))
print("After adding elements into the array:",arr1)

arr1.extend(arr2)
for i in arr1:
    print(i,end=" ")'''

# count method
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements into the list:",arr)
search=int(input("Enter the number to get count:"))
if search in arr:
    print("count is:", arr.count(search))
else:
    print("Element is not present in array")'''

# clear method
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements into the array:",arr)
arr.clear()
for i in arr:
    print(i,end=" ")

