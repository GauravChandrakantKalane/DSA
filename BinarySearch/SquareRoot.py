def squareRoot(n):
    squareRoot = 0
    start = 0
    end = n
    while(start <= end):
        mid = start + (end-start) // 2
        if(mid * mid <= n):
            squareRoot = mid
            start = mid + 1
        else:
            end = mid - 1
    return squareRoot

n = 25
print("SQUARE ROOT => ", squareRoot(n))