lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements into the list:")
for i in lst:
    print(i)

which_value_remove=int(input("enter the value which remove from list:"))
if which_value_remove in lst:
    lst.remove(which_value_remove)
    print("\n After remove the value, list look likes:")
    for i in lst:
        print(i)
else:
    print("value not found")
