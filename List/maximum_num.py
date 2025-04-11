lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

max=lst[0]
min=lst[0]
# using loop
for i in lst:
    if i>max:
        max=i
    else:
        min=i
print ("largest number is:",max)
print("smallest number is:",min)

