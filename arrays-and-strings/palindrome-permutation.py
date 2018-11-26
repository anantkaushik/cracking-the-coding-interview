"""
Given a string, write a function to check if it is a permutation of a palindrome. 
"""
import collections
def palindromePermutation(s):
    countOdd = 0
    d = collections.defaultdict(int)
    for i in s:
        d[i] += 1
        if d[i] % 2 == 1:
            countOdd += 1
        else:
            countOdd -= 1
    return countOdd <= 1