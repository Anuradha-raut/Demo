lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\nAfter adding elements in the list:")
print(lst)

mul=1
for i in lst:
    mul=mul*i
print (mul)
