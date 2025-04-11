'''lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the elements:")))

sum=0
for i in lst:
    sum=sum+i
print("sum is:",sum)

lst=[5,10,15,20,25]
print(sum(lst))'''

lst=[9,7,8,5,3,6]
for i in lst:
    sort=sorted(lst)
print(sort)