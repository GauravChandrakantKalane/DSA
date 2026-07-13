def climbStair(n):
    if(n < 0):
        return 0
    if(n == 0):
        return 1
    
    ans = climbStair(n-1) + climbStair(n-2)
    return ans

n = 3
print("ANS => ", climbStair(n))

