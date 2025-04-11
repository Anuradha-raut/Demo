lst1=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst1.append(int(input("enter the elements:")))

lst2=list(set(lst1))
print(lst2)
lst2.sort()
print("second largest element is:",lst2[-2])