def pivotElement(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while (start < end):
        mid = start + (end - start)// 2
        if(arr[0] <= arr[mid]):
            start = mid + 1
        else:
            end = mid
    return end

def searchInSortedRotatedArray(arr, target):
    n = len(arr)
    
    pivot = pivotElement(arr)

    start = 0
    end = n - 1
    if(target >= arr[0]):
        end = pivot - 1
    else:
        start = pivot
    while(start <= end):
        mid = start + (end - start) // 2
        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return -1
arr = [1,1,1,3,1]
target = 3
print("Element Index => ", searchInSortedRotatedArray(arr,target))
