lst1=[]
lst2=[]

how_many_elements=int(input("enter the how many elements you want="))
for i in range(0,how_many_elements):
    lst1.append(int(input("enter the elements:")))

lst2.extend(lst1)

print(lst2)
