def mergeArray(arr1, arr2, m , n):
    n1 = len(arr1)
    n2 = len(arr2)
    i = m - 1
    j = n - 1
    k = m + n - 1
    while(j>=0 and i>=0):
        if(arr1[i] > arr2[j]):
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    
    while(i >= 0):
        arr1[k] = arr1[i]
        i -= 1
        k -= 1
    while(j >= 0):
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    return arr1

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = 3
print("MERGED ARRAY => ", mergeArray(arr1, arr2, m, n))