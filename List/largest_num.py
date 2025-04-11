lst=[]
how_many_elements=int(input("enter the how many elements you want insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

print("\nAfter adding elements in the list:")
print(lst)

for i in lst:
    max_value = max(lst)
print("largest number is:",max_value)
