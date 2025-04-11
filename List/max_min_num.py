lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the element:")))

for i in lst:
    max_value = max(lst)
    min_value = min(lst)
print("maximum value in the list:",max_value)
print("minimum value in the list:",min_value)
