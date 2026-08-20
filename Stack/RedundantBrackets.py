def redundantBrackets(str):
    stack = []
    for i in range(len(str)):
        ch = str[i]
        if(ch == "(" or ch == "+" or ch == "-" or ch == "*" or ch == "/"):
            stack.append(ch)
        else:
            if(ch == ")"):
                isRedundant = True
                while(len(stack) != 0 and stack[-1] != "("):
                    isRedundant = False
                    stack.pop()
                if(isRedundant):
                    return True
                else:
                    stack.pop()
        
    return False