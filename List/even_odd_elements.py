lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\n After adding elements in the list:")
print(lst)

for i in lst:
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)