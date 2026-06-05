def checkPalindrome(n):
    temp = n
    reverse = 0
    while(temp != 0):
        digit = temp % 10
        reverse = reverse*10 + digit
        temp = temp // 10
    
    if(reverse == n):
        return True
    return False

n = 1321
print("IS PALINDROME => ", checkPalindrome(n))