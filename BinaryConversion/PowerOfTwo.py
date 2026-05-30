# def powerOf2(n):
#     count = 0
#     if( n <= 0):
#         return False
#     while (n != 0 ):
#         digit = n % 2
        
#         if(digit > 0):
#             count += 1
#         n = n // 2
#     if(count > 1):
#         return False
#     return True

def powerOf2(n):
    count = 0
    if( n <= 0):
        return False
    while (n != 0 ):
       if(n & 1):
            count += 1
            print("One encounter")
       n = n >> 1
    if(count > 1):
        return False
    return True  


n = 8
print("IS POWER OF 2 => ", powerOf2(n))
