from array import*

# 1.Write a Python program to create an array of 5 integers and display the array items.
# Access individual elements through indexes.

arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original array:")
for i in arr:
    print(i)

print("Access first three items individually:")
print(arr[0])
print(arr[1])
print(arr[2])

# 2.Write a Python program to append a new item to the end of the array.

arr=array('i',[1,3,5,7,9])
arr2=arr.append(11)
for i in arr:
    print(i,end=" ")

# 3. Write a Python program to reverse the order of the items in the array.

arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original Array:")
for i in arr:
    print(i,end=" ")

print("\nReverse the order of the items:")
arr2=arr.reverse()
for i in arr:
    print(i,end=" ")

#4.Write a Python program to get the current memory address and the length in elements of the buffer
# used to hold an array's contents. Also, find the size of the memory buffer in bytes.

arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original array:",arr)

  # find the current memory address of the array
memory_address=arr.buffer_info()
print("Current memory address and the length in elements of the buffer:",memory_address)
  # find size of the memory buffer
size=memory_address[1] * arr.itemsize
print("Size of the memory buffer:",size)

#5.Write a Python program to get the number of occurrences of a specified element in an array.
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original array:",arr)

print("Number of occurrences of the number 3 in the said array:")
print(arr.count(3))

