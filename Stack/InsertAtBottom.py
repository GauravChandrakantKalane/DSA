def insertAtBottom(stack,val):
    if(len(stack) == 0):
        stack.append(val)
        return stack
    
    el = stack.pop()
    insertAtBottom(stack,val)
    stack.append(el)
    return stack