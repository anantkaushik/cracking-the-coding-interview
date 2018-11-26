"""
There are three types of edits that can be performed on strings: insert a character, remove a charachter or replace a character. 
Given two strings, write a function to check if they are one edit(or xero edits) away.
"""
def oneEditAway(s1,s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    if len(s2) > len(s1):
        return oneEditAway(s2,s1)
    i,j,foundDiff = 0,0,False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if foundDiff:
                return False
            foundDiff = True
            if len(s1) == len(s2):
                j += 1
        else:
            j += 1
        i += 1
    return True