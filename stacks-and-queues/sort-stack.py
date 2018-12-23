"""
Write a program to sort a stack such that the smallest items are on the top. You can use an addittional temporary stack, but you may not copy the elements into
any other data structure(such as an array). The stack supports the following operations: push, pop, peek and isEmpty.
"""
def sort(s):
    tempStack = []
    while s:
        temp = s.pop()
        while tempStack and tempStack[-1] > temp:
            s.push(tempStack.pop())
        tempStack.push(temp)
    while tempStack:
        s.push(tempStack.pop())