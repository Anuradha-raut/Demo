#pop with index

lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("After adding elements into the list")
for i in lst:
    print(i)

indx=int(input("enter the index number to remove:"))

remove_num=lst.pop(indx)
print("\n The removed element is=",remove_num)

print("After using pop method the element looks likes:")
for i in lst:
    print (i)