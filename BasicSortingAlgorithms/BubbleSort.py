def bubbleSort(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr
    for i in range(0,n-1):
        isChanged = False
        for j in range(0,n-i-1):
            if(arr[j] > arr[j+1]):
                isChanged = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if(not isChanged):break
    return arr

arr = [1,2,3,4,5]
print("SORTED ARRAY => ", bubbleSort(arr))

# TC = 0(N2)
# SC = 0(1)