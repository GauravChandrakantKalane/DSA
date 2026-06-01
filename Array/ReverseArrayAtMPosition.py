def reverseArray(arr, m):
    start  = m + 1
    end = len(arr) - 1
    while (start <= end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr

arr = [1,2,3,4,5,6]
m = 1
print("REVERSED ARRAY AT M POSITION => ", reverseArray(arr, m))
