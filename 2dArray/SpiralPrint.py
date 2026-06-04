def spiralPrint(arr):
    rows = len(arr)
    cols = len(arr[0])
    rowStartIndex = 0
    rowEndIndex = rows - 1
    colStartIndex = 0
    colEndIndex = cols - 1
    count = 0
    total = rows * cols
    while(count < total):
        i = colStartIndex
        while(i<=colEndIndex and count < total):
            print(arr[rowStartIndex][i], end=" ")
            count += 1
            i += 1
        rowStartIndex += 1
        j = rowStartIndex
        while(j<=rowEndIndex and count < total):
            print(arr[j][colEndIndex], end=" ")
            count += 1
            j += 1
        colEndIndex -= 1
        k = colEndIndex
        while(k>=colStartIndex and count < total):
            print(arr[rowEndIndex][k], end =" ")
            count += 1
            k -= 1
        rowEndIndex -= 1
        l = rowEndIndex
        while(l>=rowStartIndex and count < total):
            print(arr[l][colStartIndex], end = " ")
            count += 1
            l -= 1
        
        colStartIndex += 1
    
arr = [[1]]
spiralPrint(arr)
        # [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
