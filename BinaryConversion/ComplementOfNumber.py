def complementOfNumber(n):
    if(n == 0):
        return 1
    complement = ~n
    bitmask = 0
    temp = n
   
    while(temp!=0):
        bitmask = bitmask << 1
        bitmask = bitmask | 1
        temp = temp >> 1
    complement = complement & bitmask
    return complement

n = 5
print("COMPLEMENT => ", complementOfNumber(n))