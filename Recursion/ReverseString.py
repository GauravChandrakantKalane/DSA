def reverseString(s,start,end):
    if(start > end):
        return
    
    temp = s[start]
    s[start] = s[end]
    s[end] = temp
    reverseString(s,start+1, end -1)
    

s = "abcd"
st = list(s)
reverseString(st,0,len(s)-1)

print("Reversed String => ", "".join(st))