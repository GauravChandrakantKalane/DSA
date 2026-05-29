def insertionSort(arr):
    n = len(arr)
    if(n == 0 or n == 1):
        return arr
    for i in range(1,n):
        element = arr[i]
        j = i-1
        while(j>=0):
            if(arr[j] > element):
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j+1] = element
    return arr

arr = [1,2,3,4,5]
print("SORTED ARRAY => ", insertionSort(arr))