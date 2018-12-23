class stackOfPlates:
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            raise NameError("Capacity should be greater than zero")
        else:
            self.capacity = capacity
        
    def push(self, item):
        if len(self.stacks) == 0:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        if len(self.stacks) == 0:
            return None 
        popData = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return popData

    def popAt(self, index):
        if len(self.stacks) == 0 or index >= len(self.stacks):
            return None
        popData = self.stacks[index][-1]
        if len(self.stacks[index]) == 1 and index == len(self.stacks) - 1:
            del self.stacks[index]
            return popData
        elif len(self.stacks[index]) == 1:
            del self.stacks[index]
        elif index == len(self.stacks) - 1:
            del self.stacks[index][-1]
            return popData
        else:
            for i in range(index+1,len(self.stacks)):
                self.stacks[index][-1] = self.stacks[index+1][0]
                for j in range(len(self.stacks[i])-1):
                    self.stacks[i][j] =  self.stacks[i][j+1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popData