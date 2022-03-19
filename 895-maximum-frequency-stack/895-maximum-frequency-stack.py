class FreqStack:

    def __init__(self):
        self.counter = Counter()
        self.stack = defaultdict(list) # {count : [ele1, ele2]}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.max_freq = max(self.max_freq, self.counter[val])
        self.stack[self.counter[val]].append(val)
        

    def pop(self) -> int:
        max_element = self.stack[self.max_freq].pop()
        self.counter[max_element] -= 1
        # If max_freq list goes empty decrease by 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1
        return max_element
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()