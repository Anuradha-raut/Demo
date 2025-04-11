lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
for i in lst:
    print(i)

lst=lst[-1:] + lst[:-1]

print("Rotated list elements looks like:")
print(lst)



