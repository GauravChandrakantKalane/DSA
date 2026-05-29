def selectionSort(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr
    for i in range(0,n-1):
        min = i
        for j in range(i,n):
            if(arr[j] <= arr[min]):
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr

arr = [17,3,5,9,1,2]
print("SORTED ARRAY => ", selectionSort(arr))

# TC = 0(N2)
# SC = 0(1)