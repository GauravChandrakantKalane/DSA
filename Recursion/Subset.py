def subset(arr, index, result, ans):
    if(index >= len(arr)):
        ans.append(result[:])
        return
    
    subset(arr,index+1,result,ans)
    result.append(arr[index])
    subset(arr,index+1,result,ans)
    result.pop()
    return ans

arr = [1,2,3]

ans = subset(arr,0,[],[])
print("FINAL ANS => ", ans)