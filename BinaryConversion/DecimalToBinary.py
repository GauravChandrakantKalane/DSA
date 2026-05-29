def decimalToBinary(n):
    power = 0
    binary = 0
    while(n != 0):
        digit = n % 2
        n = n // 2
        if(digit):
            binary =( pow(10,power)) + binary
        power+=1

    return binary

decimal = 14
print("BINARY => ",decimalToBinary(decimal))