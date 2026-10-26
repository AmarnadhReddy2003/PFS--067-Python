# Merge sort: Merge sort is an efficient, stable, and comparison-based sorting algorithm. 
# It is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, 
# and then merges the sorted halves back together. Merge sort has a time complexity of O(n log n) in all cases 
# (best, average, and worst), making it suitable for large datasets. However, it requires additional space for merging, 
# which can be a drawback for memory-constrained environments.
# we get time complexity of O(n) beacuase it involves checking of every element and we get O(log n) when we use divide and conquer rule 
# so both are combined in this mergesort so the time complexity be O(n)+ O(log n)=O(n log n)

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    # Divide array into two parts
    mid=len(arr)//2
    left=arr[:mid] # 0 to mid-1
    right=arr[mid:] # mid+1 to n-1

    # Recursively sort arrays
    left=merge_sort(left)
    right=merge_sort(right)

    # Merging two halves
    return merge(left,right)

# This method is mainly for comparision of values
def merge(left,right):
    result=[]
    i=0
    j=0
    # Compares elements from both arrays
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # Adding remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[5,2,4,1]
print(merge_sort(arr))


