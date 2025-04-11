lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))
print("\n After adding element into the list:")
for i in lst:
    print(i)

which_index_gets=int(input("enter the index number:"))
print(lst.index(which_index_gets))