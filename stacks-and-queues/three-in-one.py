"""
Describe how you could use a single array to implement three stacks.
"""
class FixedMultiStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.arr = [None] * 3 * capacity
        self.sizes = [0] * 3
        
    def push(self, stackNum, data):
        if self.sizes[stackNum] == self.capacity:
            print("Stack is already Full")
        else:
            self.sizes[stackNum] += 1
            self.arr[self.indexOfTop(stackNum)] = data
            
    def pop(self, stackNum):
        if self.sizes[stackNum] == 0:
            return "Stack is empty"
        topIndex = self.indexOfTop(stackNum)
        data = self.arr[topIndex]
        self.arr[topIndex] = None
        self.sizes[stackNum] -= 1
        return data
        
    def indexOfTop(self, stackNum):
        offset = stackNum * self.capacity
        s = self.sizes[stackNum]
        return offset + s - 1


class MultiStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * 3 * capacity
        self.top = [-1] * 3
        self.nextt = [i+1 for i in range(3*capacity)]
        self.nextt[-1] = -1
        self.free = 0
        
    def isFull(self):
        return self.free == -1
        
    def isEmpty(self, stackNum):
        return self.top[stackNum] == -1
        
    def push(self, stackNum, data):
        if self.isFull():
            print("Stack is Full")
            return
        i = self.free
        self.free = self.nextt[i]
        self.nextt[i] = self.top[stackNum]
        self.top[stackNum] = i
        self.arr[i] = data
        
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return None
        i = self.top[stackNum]
        self.top[stackNum] = self.nextt[i]
        self.nextt[i] = self.free
        self.free = i
        return self.arr[i]