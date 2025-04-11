lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\nAfter adding elements in the list")
print(lst)

if lst==[]:
    print("list is empty")
else:
    print("list is not empty")