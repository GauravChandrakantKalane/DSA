def deleteMiddleElement(stack,N,count):
    if(count == N//2):
        stack.pop()
        return stack
    
    count += 1
    val = stack.pop()
    deleteMiddleElement(stack,N,count)
    stack.append(val)
    return stack    