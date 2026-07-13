def factorial(n):
    if(n == 1):
        return 1
    ans = n * factorial(n-1)
    return  ans

n = 5
print("FACTORIAL => ", factorial(5))