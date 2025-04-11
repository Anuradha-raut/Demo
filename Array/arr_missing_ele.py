from array import*
'''arr=array('i',[])
how_many_elements=int(input("Enter the how many elements you want to insert:"))
for i in range(0,how_many_elements):
    arr.append(int(input("Enter the elements:")))
print("After adding elements into the array:",arr)

def find_missing_element(n,arr):
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    missing_element=total_sum-arr_sum
    return missing_element
print("The missing element is:",find_missing_element(5,[1,5,9,13,17]))'''

def missing_element(n,arr):
    sum_arr=sum((arr))

    expected_sum=(n*(n+1))//2
    return expected_sum - sum_arr

arr=[1,2,3,4,6]
n=6
print(missing_element(n,arr))

def missing_element(n):
    numbers=set(n)
    length=len(n)
    missing_elements=[]
    for i in range(1,n[-1]):
        if i not in numbers:
            missing_elements.append(i)
    return missing_elements

n=[1,5,9,13,17]
print(missing_element(n))
