"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
def isUnique(s):
    s = ''.join(sorted(s))
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True