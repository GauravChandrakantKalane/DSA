def subsequences(s,index,result,ans):
    if(index >= len(s)):
        if(result != ""):
            ans.append(result)
        return
    
    subsequences(s,index+1,result,ans)
    result = result+s[index]
    subsequences(s,index+1,result,ans)
    result[:-1]
    return ans

s = "abc"
print("FINAL ANS => ", subsequences(s,0,"",[]))
