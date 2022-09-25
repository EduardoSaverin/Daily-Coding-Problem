class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.elements = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.elements == self.k:
            return False
        self.q.append(value)
        self.elements += 1
        return True

    def deQueue(self) -> bool:
        if self.elements == 0:
            return False
        self.q.pop(0)
        self.elements -= 1
        return True

    def Front(self) -> int:
        if self.elements == 0:
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if self.elements == 0:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def isFull(self) -> bool:
        return self.elements == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()