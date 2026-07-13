# def solve(inputValue,index,ans,string,mapping):
#     if(index >= len(inputValue)):
#         ans.append(string)
#         return
    
#     num = int(inputValue[index])
#     val = mapping[num]
#     for char in val:
#         string+=char
#         solve(inputValue,index+1,ans,string,mapping)
#         string = string[:-1]
#     return
    





# inputValue = "23"
# ans = []
# string = ""
# mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
# solve(inputValue,0,ans,string,mapping)
# print("ANS => ", ans)



def solve(s,index,mapping,result,ans):
    if(index >= len(s)):
        ans.append(result[:])
        return 
    digit = int(s[index])
    temps = mapping[digit]
    i = 0
    while(i<len(temps)):
        result += temps[i]
        solve(s,index+1,mapping,result,ans)
        result = result[:-1]
        i+=1




s= "23"
result = ""
ans = []
mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
solve(s,0,mapping,result,ans)
print("ANS => ", ans)






