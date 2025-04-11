from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements in the array:",arr)

indx=int(input("Enter the index number which you want to replace the value:"))
value=int(input("Enter the value:"))

arr2=arr.insert(indx,value)
for i in arr:
    print(i,end=" ")