def pairSum(arr, sum):
    n = len(arr)
    ans = []
    for i in range(0, n-1):
        element  = sum - arr[i]
        for j in range(i+1,n):
            if(arr[j] == element):
                pair = []
                pair.append(min(arr[j], arr[i]))
                pair.append(max(arr[j], arr[i]))
                ans.append(pair)
        ans.sort()
    return ans

arr = [1,2,3,4,5]
sum = 5
print("PAIR OF SUM => ", pairSum(arr, sum))