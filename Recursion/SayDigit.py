def sayDigit(n, mapping):
    if(n == 0):
        return
    
    digit = n % 10
    n = n // 10
    sayDigit(n,mapping)
    print(mapping[digit])

mapping = ['zero','one','two','three','four','five','six','seven','eight','nine']
n = 45211
sayDigit(n,mapping)