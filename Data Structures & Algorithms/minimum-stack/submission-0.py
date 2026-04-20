class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)    

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.min_stack[-1]:
            return self.min_stack.pop()
        return val

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
