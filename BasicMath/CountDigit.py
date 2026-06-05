# def countDigit(n):
#     count = 0
#     while(n!=0):
#         count += 1
#         n = n // 10
#     return count

def countDigit(n):
    if(n == 0):
        return
    n = n // 10
    countDigit(n)
    count += 1

print("Count", countDigit(7621181))