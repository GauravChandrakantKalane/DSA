def swapAlternate(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr
    for i in range (0,n-1,2):
        temp  = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    return arr

arr = [1,2,3,4,5,6]
print("Swapped Array => ", swapAlternate(arr))
        