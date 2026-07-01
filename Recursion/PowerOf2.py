def powerOf2(n):
    if(n == 0):
        return 1
    
    power = 2 * powerOf2(n-1)
    return power

n = 5
print("POWER OF 2 => ", powerOf2(n))