import math
def primeNumber(n):
    primes = [True] * n
    count = 0
    sqrt = int (math.sqrt(n))
    for i in range(2,sqrt+1):
        if(primes[i]):
            for j in range(i+1,n):
                if(j%i== 0):
                    primes[j] = False
    for i in range(2,n):
        if(primes[i]):
            count += 1
    return count
n = 10
print("Number of Primes =>", primeNumber(n))