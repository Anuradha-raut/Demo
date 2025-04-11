lst1=[]
lst2=[]

how_many_elements1=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements1):
    lst1.append(int(input("enter the elements:")))

how_many_elements2=int(input("enter the how many elements you want:"))
for i in range(0,how_many_elements2):
    lst2.append(int(input("enter the elements:")))

for i in lst1:
    print(i)
for j in lst2:
    print(j)

if i==j:
    print("both lists are equal")
else:
    print("not equal")
