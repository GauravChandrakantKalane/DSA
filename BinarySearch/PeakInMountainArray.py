def peakInMountainArray(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if(arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]):
            return mid
        if(arr[mid-1] < arr[mid] and arr[mid+1] > arr[mid]):
            start = mid 
        if(arr[mid-1] > arr[mid] and arr[mid+1] < arr[mid]):
            end = mid 
    
arr = [3,9,8,6,4]
print("PEAK INDEX => ", peakInMountainArray(arr))