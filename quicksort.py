# Quicksort
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    n=len(arr)
    index=n//2
    pivot=arr[index]
    left= [x for x in arr if x<pivot]
    middle= [x for x in arr if x == pivot]
    right= [ x for x in arr if x>pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr= [10,7,1,5]
print(quick_sort(arr))
