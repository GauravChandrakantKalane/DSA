def sort012(arr):
    n = len(arr)
    countZero = 0
    countOne = 0
    countTwo = 0
    ans = []
    for i in range(0,n):
        if(arr[i] == 0):
            countZero += 1
        elif(arr[i] == 1):
            countOne += 1
        else:
            countTwo += 1
    
    while(countZero > 0):
        ans.append(0)
        countZero -= 1
    while(countOne > 0):
        ans.append(1)
        countOne -= 1
    while(countTwo > 0):
        ans.append(2)
        countTwo -= 1
    return ans

arr = [1,2,0,1,1,2,0,0,2]
print("SORTED => ", sort012(arr))