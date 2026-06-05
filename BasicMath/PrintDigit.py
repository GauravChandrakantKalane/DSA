# def printDigit(n):
#     while (n != 0):
#         digit = n % 10
#         n = n // 10
#         print("Digit => ", digit)

def printDigit(n):
    if(n == 0):
        return
    digit = n % 10
    n = n // 10
    print("Digit => ", digit)
    printDigit(n)
    
printDigit(1563)