def factorial(n):
    if(n == 1):
        return 1
    
    
    ans = n * factorial(n-1)
    return ans

    
ans = 1
n = 5
print("FACTORIAL OF ", n, " -> ", factorial(n))