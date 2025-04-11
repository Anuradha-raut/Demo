lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\nThe given list is:")
print(lst)

print("\nRotated list from 1th position:")
for i in lst:
    lst2 = lst[2:] + lst[:2]
print(lst2)


