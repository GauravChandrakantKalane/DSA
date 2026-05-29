import math
def binaryToDecimal(n):
    decimal = 0
    power = 0
    while(n != 0):
        digit = n % 10
        if(digit):
            decimal = decimal + (pow(2,power))
        n = n // 10
        power += 1
    return decimal

binary = 111
print("DECIMAL => ", binaryToDecimal(binary))