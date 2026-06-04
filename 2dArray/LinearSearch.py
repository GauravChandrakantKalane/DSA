def linearSearch(arr, target):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(0,rows):
        for j in range(0,cols):
            if(target == arr[i][j]):
                return True
    
    return False

arr = [[1,2,3],[4,5,6],[7,8,9]]
target = 14
print("IS PRESENT => ", linearSearch(arr,target))