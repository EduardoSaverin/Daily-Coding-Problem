class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.arr = [None]*(self.size)
        
    def hash(self, key):
        return key  % self.size

    def add(self, key: int) -> None:
        h = self.hash(key)
        if self.arr[h] is None:
            self.arr[h] = [key]
        else:
            self.arr[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if self.arr[h] is not None:
            while key in self.arr[h]:
                self.arr[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        if self.arr[h] is not None:
            return key in self.arr[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)