import math
def divisors(n):
    ans = []
    sqrt = int (math.sqrt(n))
    for i in range(1,sqrt+1):
        if(n%i == 0):
            ans.append(i)
            if(i != n//i):
                ans.append(n//i)

    return ans

n = 27
print("Divisors => ", divisors(n))