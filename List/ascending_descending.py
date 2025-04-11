lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the element:")))
print("\n After adding elements in the lst:")
for i in lst:
    print(i)

print("\n Ascending order:")
for i in lst:
    lst.sort(reverse=False)
print(lst)

print("\n Descending order:")
for i in lst:
    lst.sort(reverse=True)
print(lst)