def sort01(arr):
    n = len(arr)
    i = 0
    j = n - 1
    while (i < j):
        if(arr[i] == 1 and arr[j] == 0):
            temp  = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
        elif(arr[i] == 0 and arr[j] == 0):
            i += 1
        elif(arr[i] == 1 and arr[j] == 1):
            j += 1
        else:
            i += 1
            j += 1
            
    return arr

arr = [0,1,0,1,0,0,1,1]
print("SORTED ARRAY => ", sort01(arr))