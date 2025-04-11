from array import*
arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("Original Array:",arr)

for i in arr:
    if i%2==0:
        #print(i)
        print("Even elements:",i,end=" ")

    else:
       print("Odd elements:",i,end=" ")