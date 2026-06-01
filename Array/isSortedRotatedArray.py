def isSortedRotatedArray(arr):
    n = len(arr)
    count = 0
    for i in range(0,n-1):
        if(arr[i] > arr[i+1]):
            count += 1
    
    if(arr[n-1] > arr[0]):
        count += 1
    
    if(count <= 1):
        return True
    else:
        return False

arr = [1,1,1]
print("IS SORTED AND ROTATED ARRAY => ", isSortedRotatedArray(arr))