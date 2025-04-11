from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in the array:",arr)

# Convert the array into ascending order
arr2=sorted(arr)
print("\n Ascending order:")
print(arr2)

# Convert the array into descending order
arr2=sorted(arr, reverse=True)
print("\n Descending order:")
print(arr2)

