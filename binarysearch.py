# Binary Search: Binary search is an efficient search algorithm that works on sorted lists. 
# It repeatedly divides the search interval in half, eliminating half of the remaining elements until the target value is found or the interval is empty.
# It works on divide and conquer principle.I t is more efficient than linear search for larger data sets.
def binary_search(arr,target):
    arr=sorted(arr)
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[10,-20,30,-40,50,-60]
target=-60
result=binary_search(arr,target)
print('Element found at Index',result)

 