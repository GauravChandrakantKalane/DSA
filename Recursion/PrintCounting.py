def printCounting(n):
    if(n == 0):
        return
    printCounting(n-1)
    print(n)
    return

n = 5
printCounting(n)