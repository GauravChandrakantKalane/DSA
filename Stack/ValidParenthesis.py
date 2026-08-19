def validParenthesis(s):
    n = len(s)
    if(n == 0 or n % 2 != 0):
        return False
    if(s[0] == "}" or s[0] == ")" or s[0] == "]"):
        return False
    stack = []
    i = 0
    while(i<n):
        ch = s[i]
        if(ch == "{" or ch == "(" or ch == "["):
            stack.append(ch)
        else:
            if(len(stack) == 0):
                return False
            else:
                if((ch=="}" and stack[-1] == "{") or (ch==")" and stack[-1] == "(") or (ch=="]" and stack[-1] == "[")):
                    stack.pop()
                else:
                    return False
        i+=1
    
    if(len(stack) == 0):
        return True
    else:
        return False
