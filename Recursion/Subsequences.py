def subsequences(s,index,result,ans):
    if(index >= len(s)):
        if(result != ""):

            ans.append(result)
        return
    
    subsequences(s,index+1,result,ans)
    result += s[index]
    subsequences(s,index+1,result,ans)
    result[:-1]

s = "ab"
result = ""
ans = []
subsequences(s,0,result,ans)
print("ANS => ", ans)