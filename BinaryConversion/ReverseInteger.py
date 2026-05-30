def reverseInteger(n):
    reverse = 0
    isNegative = False
    if(n < 0):
        n = n * -1
        isNegative = True
    while(n != 0):
        digit = n % 10
        n = n // 10
        if((reverse * 10 < -2 ** 31) or (reverse * 10 > 2 ** 31 -1)):
            return 0
        reverse = (reverse * 10) + digit
    if(isNegative):
        reverse = reverse * -1
        return reverse
    return reverse

n = -98771837483
print("REVERSE INTEGER => ", reverseInteger(n)) 