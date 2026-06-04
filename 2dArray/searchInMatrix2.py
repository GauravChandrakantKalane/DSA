def searchMatrix(arr,target):
    rows = len(arr)
    cols = len(arr[0])

    rowIndex = 0
    colIndex = cols - 1
    while(rowIndex < rows and colIndex >= 0):
        element = arr[rowIndex][colIndex]
        if(target == element):
            return True
        elif(target > element):
            rowIndex += 1
        else:
            colIndex -= 1
    return False

arr = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 85
print("IS PRESENT => ", searchMatrix(arr,target))