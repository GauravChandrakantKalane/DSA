def partition(arr,start,end):
    pivotElement = arr[start]
    smallCount = 0
    for i in range(start+1,end+1):
        if(arr[i] < pivotElement):
            smallCount += 1
    # Put pivot Element at it's right position
    pivotPosition = smallCount + start
    temp = arr[pivotPosition]
    arr[pivotPosition] = pivotElement
    arr[start] = temp

    i = start
    j = end
    while(i < pivotPosition and j > pivotPosition):
        while(arr[i] < pivotElement and i < pivotPosition):
            i+=1
        while(arr[j] > pivotElement and j > pivotPosition):
            j-=1
        if(i < pivotPosition and j > pivotPosition):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
    return pivotPosition



def quickSort(arr, start, end):
    if(start >= end):
        return
    
    pivot = partition(arr,start,end)
    quickSort(arr,start,pivot-1)
    quickSort(arr,pivot+1,end)

arr = [8,4,2,1,0,3]
quickSort(arr, 0, len(arr)-1)
print("SORTED ARRAY => ", arr)