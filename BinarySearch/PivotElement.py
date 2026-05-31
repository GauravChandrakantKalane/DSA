# This could be used as pivot or the smallest/largest element in the sorted rotated array
def pivotElement(arr):
    n = len(arr)
    start  = 0
    end = n - 1
    while (start < end):
        mid = start + (end-start) // 2
        if(arr[0] <= arr[mid]):
            start = mid + 1
        else:
            end = mid
    return end

arr = [4,6,8,1,2,3]
print("PIVOT => ", pivotElement(arr))