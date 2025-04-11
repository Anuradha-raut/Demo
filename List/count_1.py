lst=[]
how_many_elements=int(input("enter the how many elements you want:"))
for i in range(0, how_many_elements):
    lst.append(int(input("enter the elements:")))

search=int(input("enter the number to get count:"))

if search in lst:
    print(lst.count(search))
else:
    print("element not present")