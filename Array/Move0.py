def move0(arr):
    n = len(arr)
    i = 0
    j = 0
    while(i < n and j < n):
        if(arr[i] == 0 and arr[j]> 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
        else:
            j += 1
    return arr

arr = [0,1,0,3,2,0,0]
print("ANSWER => ", move0(arr))
