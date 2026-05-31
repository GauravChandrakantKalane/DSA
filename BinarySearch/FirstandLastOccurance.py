
def firstOccurance(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    pos = -1
    while (start <= end):
        mid = start + (end - start) // 2
        if(arr[mid] == target):
            pos = mid
            end = mid - 1
        elif(arr[mid] > target):
            end = mid - 1
        else: 
            start = mid + 1
    return pos

def lastOccurance(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    pos = -1
    while (start <= end):
        mid = start + (end - start ) // 2
        if(arr[mid] == target):
            pos = mid
            start = mid + 1
        elif(arr[mid] > target):
            end = mid - 1
        else: 
            start = mid + 1
    return pos

def firstandlastoccurance(arr, target):
    
    first = firstOccurance(arr, target)
    last = lastOccurance(arr,target)
    return [first, last]

arr = [1,2,3,3,3,3,4,5,6,6,6,6,6,6]
target = 3
print("FIRST AND LAST OCCURANCE => ", firstandlastoccurance(arr,target))