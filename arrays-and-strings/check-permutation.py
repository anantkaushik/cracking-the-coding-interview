"""
Given two strings write a method to decide if one is a permutation of the other.
"""
import collections
def permutationCheck(s1,s2):
    if len(s1) != len(s2):
        return False
    letters = collections.defaultdict(int)
    for i in s1:
        letters[i] += 1
    for i in s2:
        letters[i] -= 1
        if letters[i] < 0:
            return False
    return True