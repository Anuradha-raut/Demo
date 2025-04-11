lst=[]
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0, how_many_elements):
    lst.append(int(input("enter the elements=")))

indx=int(input("enter the index location:"))
value=int(input("enter the value:"))

lst.insert(indx,value)
for i in lst:
    print (i)