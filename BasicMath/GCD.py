def gcd(a,b):
    while (a > 0 and b > 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
    if(a == 0):
        return b
    else:
        return a

a = 14
b = 21

print("GCD IS => ", gcd(a,b))
