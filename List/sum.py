lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

sum=0
for i in lst:
    sum=sum+i
print("sum is:",sum)