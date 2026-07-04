
def merge(arr,start,mid,end):
    lenArr1 = mid - start + 1
    lenArr2 = end - mid
    arr1 = [0] * lenArr1
    arr2 = [0] * lenArr2

    i = 0
    while(i<lenArr1):
        arr1[i] = arr[start + i]
        i+=1
    i = 0
    while(i<lenArr2):
        arr2[i] = arr[mid+1+i]
        i+=1
    
    i = 0
    j = 0
    k = start

    while(i < lenArr1 and j < lenArr2):
        if(arr1[i] < arr2[j]):
            arr[k] = arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    while(i < lenArr1):
        arr[k] = arr1[i]
        i+=1
        k+=1
    while(j < lenArr2):
        arr[k] = arr2[j]
        j+=1
        k+=1

def mergeSort(arr,start,end):
    if(start >= end):
        return
    
    mid = start + (end-start) // 2
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,mid,end)

arr = [8,4,2,1,0,3]
mergeSort(arr,0,len(arr)-1)
print(arr)
