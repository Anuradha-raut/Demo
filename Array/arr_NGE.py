#Next Greater Element

from array import*
arr=array('i',[11,23,32,3])

for i in range(0,len(arr)):
    next=-1
    for j in range(i+1,len(arr)):
        if arr[i] < arr[j]:
            next=arr[j]
            break
    print(str(arr[i]) + "---->" +str(next))
