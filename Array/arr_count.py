from array import*

arr1=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr1.append(int(input("Enter the elements:")))

count_of_10=arr1.count(10)
print("10-------->",count_of_10)

count_of_20=arr1.count(20)
print("20-------->",count_of_20)

count_of_30=arr1.count(30)
print("30-------->",count_of_30)

count_of_50=arr1.count(50)
print("50--------->",count_of_50)
