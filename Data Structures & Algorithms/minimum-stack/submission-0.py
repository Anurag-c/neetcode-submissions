class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return
        
        # if val < min, pushes -ve, indicating change in min
        self.stack.append(val - self.min) 
        self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack[-1]
        self.stack.pop()
        self.min = self.min - min(0, val)
        
    def top(self) -> int:
        return self.min + max(0, self.stack[-1])
        
    def getMin(self) -> int:
        return self.min
