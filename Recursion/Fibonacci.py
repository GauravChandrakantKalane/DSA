def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    ans = fibonacci(n-1) + fibonacci(n-2)
    return ans

n = 8
print(fibonacci(n))
    
    
    
    