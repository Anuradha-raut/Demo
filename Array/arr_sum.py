from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("enter the elements:")))
print("After adding elements in the array:",arr)
sum=0
for i in arr:
    sum=sum+i
print("sum of all elements in array:",sum)
