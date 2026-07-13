
# For Array
# def checkPalindromeForArray(s,start,end):
#     if(start >= end):
#         return True
    
#     if(s[start] == s[end]):
#         return checkPalindrome(s,start+1,end-1)
#     else:
#         return False



# For Number
# convert the number to binary and convert that to string and compare
def binary(n):
    
    ans = ""
    while(n!=0):
        bit = n & 1
        ans = str(bit) + ans
        n = n >> 1
    return ans
def checkPalindrome(str,start,end):
    if(start>=end):
        return True
    if(str[start] == str[end]):
        return checkPalindrome(str,start+1,end-1)
    else:
        return False

n = 4
bin = binary(n)
print("BIN => ", bin)
print("IS PALINDROME => ", checkPalindrome(bin,0,len(bin)-1))
    


    

# s = ['h','e','e','h']
# print("Palindrome StringArray => ", checkPalindromeForArray(s,0,len(s)-1))