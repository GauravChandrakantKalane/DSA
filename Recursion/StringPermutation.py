def solve(arr,index,ans):
    if(index >= len(arr)):
        ans.append(arr[:])
        return 
    
    for i in range(index,len(arr)):
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
        solve(arr,index+1,ans)
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
    return

arr =[1,2,3]
ans = []
solve(arr,0,ans)
print("ANSWER => ", ans)