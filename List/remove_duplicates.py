lst=[]
how_many_elements=int(input("enter the how many elements you want insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
print(lst)

for i in lst:
    lst=list(set(lst))
print("\n removed duplicates list looks like this:")
print(lst)