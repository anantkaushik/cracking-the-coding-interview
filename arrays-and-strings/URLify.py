"""
Write a method to replace all the spaces in a string S with ‘%20’. You may assume that the string has sufficient space 
at the end to hold the additional characters, and that you are given the "true" length of the string.
"""
def replaceSpaces(s, length):
    s = list(s)
    count = 0
    for i in range(length):
        if s[i] == ' ':
            count += 1
    index = length + count*2
    for i in range(length-1, -1, -1):
        if s[i] == " ":
            s[index-1] = "0"
            s[index-2] = "2"
            s[index-3] = "%"
            index -= 3
        else:
            s[index-1] = s[i]
            index -= 1
    return "".join(s)      
    
print(replaceSpaces("Mr John Smith    ",13))