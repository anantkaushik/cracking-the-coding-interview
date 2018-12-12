"""
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
"""
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        
    def pop(self):
        n = self.stack.pop()
        if self.min_stack[-1] == n:
            self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min_stack[-1]