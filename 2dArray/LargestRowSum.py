def largestRowSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    rowIndex = -1
    rowSum = 0
    for i in range(0,rows):
        sum = 0
        for j in range(0,cols):
            sum += arr[i][j]
        if(rowSum < sum):
            rowIndex = i
            rowSum = sum
    return rowIndex

arr = [[1,2,3],[7,8,9],[4,5,6]]
print("Largest Row Sum is => ", largestRowSum(arr))