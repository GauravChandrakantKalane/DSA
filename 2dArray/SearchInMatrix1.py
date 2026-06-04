def searchInMatrix(arr, target):
    rows = len(arr)
    cols = len(arr[0])

    start = 0
    end = rows * cols - 1
    while(start <= end):
        mid = start + (end - start) // 2
        element = arr[mid // cols][ mid % cols]
        if(target == element):
            return True
        elif(target > element):
            start = mid + 1
        else:
            end = mid - 1
    return False

arr = [[1,2,3],[4,5,6],[7,8,9]]
print("IS PRESENT => ", searchInMatrix(arr,15))