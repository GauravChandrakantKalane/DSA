# Armstrong number for 3 digit number
def armstrongNumber(n):
    temp = n
    sum = 0
    while (temp != 0):
        digit = temp % 10
        sum = sum + (digit ** 3)
        temp = temp // 10
    if(sum == n):
        return True
    return  False

n = 
print("Is Armstrong => ", armstrongNumber(n))