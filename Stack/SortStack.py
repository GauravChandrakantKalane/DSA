def insert(stack,el):
    if(len(stack) == 0):
        stack.append(el)
        return stack
    
    if(stack[-1] > el):
        val = stack.pop()
        insert(stack,el)
        stack.append(val)
    else:
        stack.append(el)
    return stack

def sortStack(s):
    if(len(s) == 0):
        return
    
    el = s.pop()
    sortStack(s)
    insert(s,el)
    return s