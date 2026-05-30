def uniqueElement(arr):
    n = len(arr)
    element = 0
    for i in range(0,n):
        element = element ^ arr[i]
    return element

arr = [2 ,3, 1, 6, 1, 6, 2]
print("Unique Element => ", uniqueElement(arr))
        