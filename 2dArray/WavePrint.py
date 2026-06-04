def wavePrint(arr):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(0,cols):
        if(i%2 == 0):
            for j in range(0,rows):
                print(arr[j][i], end =" ")
        else:
            for j in range(rows-1,-1,-1):
                print(arr[j][i], end = " ")
        print(end ="")
    
arr = [[1,2,3],[4,5,6],[7,8,9]]
wavePrint(arr)