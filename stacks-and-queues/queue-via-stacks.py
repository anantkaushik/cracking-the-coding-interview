"""
Implement a MyQueue class which implements a queue using two stacks.
"""
class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        self.s1.append(x)
        

    def pop(self):
        self.shiftStack()
        return self.s2.pop()
        

    def peek(self):
        self.shiftStack()
        return self.s2[-1]
        

    def empty(self):
        return True if (len(self.s1)+len(self.s2)) <= 0 else False

    def shiftStack(self):
        if len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())