lst1=[]
how_many_elements=int(input("enter the how many elements you want to insert in list1:"))
for i in range(0,how_many_elements):
    lst1.append(int(input("enter the elements:")))

lst2=[]
how_many_elements=int(input("enter the how many elements you want to insert in list2:"))
for i in range(0,how_many_elements):
    lst2.append(int(input("enter the elements:")))

print("\n Merge list1 and list2:")
lst=lst1+lst2
print(lst)

print("\n Merged list in descending order looks like as:")
for i in lst:
    lst.sort(reverse=True)
print(lst)
