
# For Array
def checkPalindromeForArray(s,start,end):
    if(start >= end):
        return True
    
    if(s[start] == s[end]):
        return checkPalindrome(s,start+1,end-1)
    else:
        return False



# For Number
# convert the number to binary and convert that to string and compare
def binary(n):
    while(n!=0):
        print("n>>1", n >> 1)
        n = n >> 1
binary(5)
def checkPalindrome(n,start,end):
    if(start>=end):
        return True
    


    

s = ['h','e','e','h']
print("Palindrome StringArray => ", checkPalindromeForArray(s,0,len(s)-1))