from numpy import*
# using relational operators

# greater than(>):
arr1=array([1,2,3,4])
arr2=array([5,6,7,8])
result=arr1>arr2
print("arr1 is greater than arr2:",result)

# less than(<):
arr1=array([1,2,3,4])
arr2=array([5,6,7,8])
result=arr1<arr2
print("arr1 is less than arr2:",result)

# greater than equal to
arr1=array([5,4,6,3])
arr2=array([1,4,8,3])
result=arr1>=arr2
print("arr1 is greater than or equal to arr2:",result)

# less than equal to
arr1=array([2,3,1,4])
arr2=array([8,7,9,6])
result=arr1<=arr2
print("arr1 is less than or equal to arr2:",result)

# double equal to
arr1=array([1,2,3,4])
arr2=array([1,5,8,4])
result=arr1==arr2
print("arr1 is equal to arr2:",result)

# any()
arr1=array([1,2,3])
arr2=array([4,3,6])
result=arr1>arr2
print("Any result=",any(result))

# all()
arr1=array([9,8,7])
arr2=array([4,3,6])
result=arr1>arr2
print("All result=",all(result))