def linearSearch(arr, target):
    for i in range (0, len(arr)):
        if(arr[i] == target):
            return i
    return -1

arr = [1,2,3,4,5,6]
print("Number Index in Array => ", linearSearch(arr,40))