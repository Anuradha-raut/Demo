lst=[]
how_many_elements=int(input("enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    lst.append(int(input("enter the element:")))
print("\n After adding elements in the list:")
for i in lst:
    print(i)

print("Count of 10=")
for i in lst:
    count=lst.count(10)
print(count)

print("count of 20=")
for i in lst:
    count=lst.count(20)
print(count)

print("count of 30=")
for i in lst:
    count=lst.count(30)
print(count)

print("count of 50=")
for i in lst:
    count=lst.count(50)
print(count)
