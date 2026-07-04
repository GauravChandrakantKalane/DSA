def reverseString(s,start,end):
    if(start > end):
        return
    
    temp = s[start]
    s[start] = s[end]
    s[end] = temp
    reverseString(s,start+1, end -1)
    return s

s = ['h','e','l','l']
print("Reversed String => ", reverseString(s,0,len(s)-1))