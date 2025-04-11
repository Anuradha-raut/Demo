from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in the array:",arr)

arr2=arr.reverse()
for i in arr:
    print(i,end=" ")

