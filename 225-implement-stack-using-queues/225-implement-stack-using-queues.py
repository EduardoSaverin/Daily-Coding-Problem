class MyStack:

    def __init__(self):
        self.q = []
        self.temp = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        
    def pop(self) -> int:
        for index in range(len(self.q)-1):
            self.temp.append(self.q[index])
        value = self.q[-1]
        self.q = self.temp
        self.temp = []
        return value
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()