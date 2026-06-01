def reverse(arr):
    i = 0
    j = len(arr) - 1
    while(i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return arr

def addArray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    carry = 0
    ansArr = []
    i = n1 - 1
    j = n2 - 1
    while(i >= 0 and j >= 0):
        sum = arr1[i] + arr2[j] + carry
        if(sum >= 10):
            ans = sum % 10
            carry = sum // 10
            ansArr.append(ans)
        else:
            ansArr.append(sum)
            carry = 0
        i -= 1
        j -= 1
    
    while (i >= 0):
        sum = arr1[i] + carry
        if(sum >= 10):
            ans = sum % 10
            carry = sum // 10
            ansArr.append(ans)
        else:
            ansArr.append(sum)
            carry = 0
        i -= 1

    while (j >= 0):
        sum = arr2[j] + carry
        if(sum >= 10):
            ans = sum % 10
            carry = sum // 10
            ansArr.append(ans)
        else:
            ansArr.append(sum)
            carry = 0
        j -= 1
    if(carry > 0):
        ansArr.append(carry)

    return reverse(ansArr)

arr1 = [9,9,9]
arr2 = [9,9,9]
print("Added Array => ", addArray(arr1, arr2))
