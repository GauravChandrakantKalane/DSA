def rowWiseSum(arr):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(0,rows):
        sum = 0
        for j in range(0,cols):
            sum += arr[i][j]
        print("SUM OF ",i," row => ", sum)

def colWiseSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    for i in range(0,cols):
        sum = 0
        for j in range(0,rows):
            sum += arr[j][i]
        print("SUM OF ",i," col => ", sum)

    
arr = [[1,2,3],[4,5,6],[7,8,9]]
rowWiseSum(arr)
print("----------")
colWiseSum(arr)