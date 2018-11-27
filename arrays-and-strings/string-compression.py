"""
Implememnt a method to perform basic string string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only
uppercase and lowercase letters(a-z). 
"""
def compress(s):
    compressed = []
    countConsecutive = 0
    i = 0
    while i < len(s):
        ch = s[i]
        while i < len(s) and s[i] == ch:
            countConsecutive += 1
            i += 1
        compressed.append(ch)
        compressed.append(str(countConsecutive))
        countConsecutive = 0
    res = "".join(compressed)
    return res if len(s) > len(res) else s