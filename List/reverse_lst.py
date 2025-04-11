# reverse using reverse method:

'''lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
for i in lst:
    print(i)

lst.reverse()

print("\n After reverse the elements in the list:")
for i in lst:
    print(i)'''

# reverse using slicing:
lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
for i in lst:
    print(i)

lst2=lst[::-1]

print("\n After reverse the list the list looks like:")
for i in lst2:
    print(i)