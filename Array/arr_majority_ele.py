from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original array:",arr)
n= len(arr)
for i in arr:
    if arr.count(i) > n/2:
        print("There are Majority Elements in the given array.")
    else:
        print("There are no Majority Elements in the given array.")

