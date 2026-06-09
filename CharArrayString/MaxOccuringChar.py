def maxOccuringChar(s):
    wordsArr = [0] * 26
    max = -1
    for i in range(0,len(s)):
        pos =ord(s[i]) - ord('a') 
        wordsArr[pos] += 1
    
    for i in range(0,len(wordsArr)):
        if(wordsArr[i] > wordsArr[max]):
            max = i
    print("MAX ", max)
    char = chr(max + ord('a'))
    return char

s = "gaurav"
print("Maximum Occuring Character => ", maxOccuringChar(s))