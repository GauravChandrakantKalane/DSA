# Remove all spaces and replace them with @40
def replaceSpaces(s):
    ans = ""
    for char in s:
        if(char != " "):
            ans += char
        else:
            ans += '@40'
    return ans

s = " Hello my friend"
print("Replaced String => ", replaceSpaces(s))