def minCostToMakeStringValid(str):
    n = len(str)
    if(n%2 != 0):
        return -1
    stack = []
    for i in range(n):
        ch = str[i]
        if(ch == "{"):
            stack.append(ch)
        else:
            if(len(stack) != 0 and stack[-1] == "{"):
                stack.pop()
            else:
                stack.append(ch)

    a = 0
    b = 0
    z = len(stack)
    for i in range(z):
        if(stack[i] == "{"):
            a += 1
        else:
            b += 1

    ans = (a+1)//2 + (b+1)//2
    return ans 