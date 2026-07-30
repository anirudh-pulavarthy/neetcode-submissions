class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_index:
            self.min_index.append(0)
        else:
            if val < self.stack[self.min_index[-1]]:
                self.min_index.append(len(self.min_index))
            else:
                self.min_index.append(self.min_index[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_index.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index[-1]]
