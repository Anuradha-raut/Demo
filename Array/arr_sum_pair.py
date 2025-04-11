from array import*

arr=array('i',[1,2,3,4,5])
sum=7
len=len(arr)
for i in range(len):
    for j in range(i,len):
        if arr[i]+arr[j]==sum:
            print("pairs whose sum is 7:",arr[i],arr[j])
            #print(arr[i],arr[j])

