from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("The original array is:",arr)

print("The rotated array is:")
print((arr[4:])+(arr[:4]))
