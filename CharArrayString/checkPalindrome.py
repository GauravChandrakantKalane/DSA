def lower(s):
    n = len(s)
    lower = ''
    for i in range(0,n):
        if(s[i] >= 'A' and s[i] <= 'Z'):
            char = chr(ord(s[i]) - ord('A') + ord('a'))
            lower = lower + (char)
        else:
            lower = lower + s[i]
    return lower

s = 'ARRAY'

def filter(s):
    n = len(s)
    filtered = ''
    for i in range(0,n):
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >='a' and s[i] <='z') or ((s[i]) >= '0' and (s[i]) <= '9')):
            filtered = filtered + s[i]
    return filtered

def checkPalindrome(s):
    filtered = filter(s)
    print("FILTERD => ", filtered)
    n = len(filtered)
    if(n == 0 or n == 1):
        return TRUE
    lowerFiltered = lower(filtered)
    print("LOWERED FILTERED => ", lowerFiltered)
    for i in range(0, n // 2 + 1):
        if(lowerFiltered[i] != lowerFiltered[n-i-1]):
            return False
    return True

s = 'c1 O$d@eeD o1c'    
print("IS PALINDROME => ", checkPalindrome(s))
