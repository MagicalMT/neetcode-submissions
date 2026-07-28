class MinStack:

    def __init__(self):
        self.l = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.min_num:
            self.min_num.append(val)
        else:
            self.min_num.append(min(self.min_num[-1], val))

    def pop(self) -> None:
        self.l.pop()
        self.min_num.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
