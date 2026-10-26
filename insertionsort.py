#Insertion Sort: Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. 
# It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 
# However, insertion sort provides several advantages such as simple implementation, efficient for small data sets, 
# adaptive (efficient for data sets that are already substantially sorted), stable (does not change the relative order 
# of elements with equal keys), and in-place (only requires a constant amount O(1) of additional memory space).

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[9,9,8,4,5,6,8,3]
print(insertion_sort(arr))