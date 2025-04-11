# sort by ascending order

'''lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))


print("\n After adding the elements in list:")
for i in lst:
    print(i)

lst.sort()

print("\n after sort the list by ascending order:")
for i in lst:
    print(i)'''


# sort by descending order:

lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding the elements in list:")
for i in lst:
    print(i)

lst.sort(reverse=True)

print("\n After sort the elements in descending order the list looks like:")
for i in lst:
    print(i)