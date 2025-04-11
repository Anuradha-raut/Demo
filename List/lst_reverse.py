'''lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
print(lst)

print("\n Reverse list:")
for i in lst:
    lst.reverse()
print(lst)'''

lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n Reverse list:")
for i in lst:
    lst2 = lst[::-1]
print(lst2)



