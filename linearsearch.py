# Searching Algorithms

# 1. Linear Search
# 2. Binary Search
# Linear Search: Linear search is a simple search algorithm that checks every element in the list until it finds the target value. 
# # It is not efficient for large datasets but works well for small lists.  

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[10,20,30,40,50] 
target=50
result=linear_search(arr,target)
if result !=-1:
    print("Element found at Index: ",result)
else:
    print('Element not found in the list')
    