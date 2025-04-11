from array import*
typecode=input("Enter the typecode(i,f,u)=")
arr=array(typecode,[])

if typecode=='i':
    how_many_elements=int(input("Enter the limit of the array:"))
    for i in range(0,how_many_elements):
        arr.append(int(input("Enter the elements:")))
elif typecode=='f':
    how_many_elements=int(input("Enter the limit of the array:"))
    for i in range(0,how_many_elements):
        arr.append(float(input("Enter the elements:")))
elif typecode=='u':
    how_many_elements=int(input("Enter the limit of the array:"))
    for i in range(0,how_many_elements):
        arr.append(input("Enter the elements:"))
else:
    print("Please enter correct typecode")

print("The following array elements:")
for i in arr:
    print(i,end=" ")