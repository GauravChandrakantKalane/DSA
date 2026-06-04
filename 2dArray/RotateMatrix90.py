def rotateMatrix(arr):
    rows = len(arr)
    cols = len(arr[0])

    # Transpose
    for i in range(0,rows):
        for j in range(i,cols):
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[i][j] = temp
    
    for i in range(0,rows):
        for j in range(0,cols // 2):
            temp = arr[i][j]
            arr[i][j] = arr[i][j-i-1]
            arr[i][j-i-1] = temp
    return arr

arr = [[1,2,3],[4,5,6],[7,8,9]]
print("ROTATED ARRAY => ", rotateMatrix(arr))