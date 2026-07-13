def subset(arr,index,result,ans):
    if(index >= len(arr)):
        ans.append(result[:])
        return
    
    subset(arr,index+1,result,ans)
    result.append(arr[index])
    subset(arr,index+1,result,ans)
    result.pop()
    return

str = "ab"
result = []
ans = []
subset(str,0,result,ans)
print("ANS => ", ans)