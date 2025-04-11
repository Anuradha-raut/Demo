from array import*

arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original array:",arr)


arr_1=sorted(arr)
print(arr_1)
print("The second largest element is:",arr_1[-2])
