
def partition(arr,start,end):
    el = arr[start]
    minCount = 0
    i = start+1
    while(i<=end):
        if(arr[i] < el):
            minCount += 1
        i+=1
    # swap the el to it's correct position
    pivot = start+minCount
    arr[start] = arr[pivot]
    arr[pivot] = el
    i = start
    j = end
    while(i < pivot and j > pivot):
        while(i<pivot and arr[i]<el):
            i+=1
        while(j > pivot and arr[j]>el):
            j-=1
        if(i < pivot and j > pivot):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
    return pivot


def quickSort(arr,start,end):
    if(start >= end):
        return 
    
    pivot = partition(arr,start,end)
    quickSort(arr,start,pivot-1)
    quickSort(arr,pivot+1,end)

arr = [5,7,2,3,9]
print("UNSORTED ARRAY => ", arr)
quickSort(arr,0,len(arr)-1)
print("SORTED ARRAY => ", arr)