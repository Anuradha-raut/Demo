lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\nThe given list is:")
print(lst)
sum=15
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]+lst[j]==sum:
            print(lst[i])
        else:
            print(lst[j])


