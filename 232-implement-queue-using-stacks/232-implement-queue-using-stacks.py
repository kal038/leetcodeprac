class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
                

    def pop(self) -> int:
        if len(self.s2) == 0:
            self.transfer()
        return self.s2.pop(-1)

    def peek(self) -> int:
        if len(self.s2) == 0:
            self.transfer()
        print(self.s2)
        return self.s2[-1]

    def empty(self) -> bool:
        return (len(self.s1) == 0 and len(self.s2) == 0)
    
    def transfer(self):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop(-1))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()