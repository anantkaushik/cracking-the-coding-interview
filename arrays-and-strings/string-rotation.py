"""
Assume you have a method isSubstring which checks if one  word is a substring of another. Given two strings, 
s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring(eg. "waterbottle" is a 
rotation of "erbottlewat".)
"""
def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    newS = s1 + s1
    return s2 in newS # Alternative of IsSubstring method.
