def solve(inputValue,index,ans,string,mapping):
    if(index >= len(inputValue)):
        ans.append(string)
        return
    
    num = int(inputValue[index])
    val = mapping[num]
    for char in val:
        string+=char
        solve(inputValue,index+1,ans,string,mapping)
        string = string[:-1]
    return
    





inputValue = "23"
ans = []
string = ""
mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
solve(inputValue,0,ans,string,mapping)
print("ANS => ", ans)