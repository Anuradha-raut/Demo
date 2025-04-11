#pop without index

lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("After addding elements into the list:")
for i in lst:
    print(i)

remove_num=lst.pop()
print("\n The removed element is=",remove_num)

print("After use of pop method the elements looks likes:")
for i in lst:
    print(i)

