class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.arr = [None]*self.size
        
    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        if self.arr[h] is not None:
            for index, ls in enumerate(self.arr[h]):
                k,v = ls
                if key == k:
                    self.arr[h][index] = [k, value]
                    return
            self.arr[h].append([key, value])
        else:
            self.arr[h] = [[key, value]]
                    

    def get(self, key: int) -> int:
        ls = self.arr[self.hash(key)]
        if not ls:
            return -1
        for k,v in ls:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        ls = self.arr[h]
        if not ls:
            return
        for index, l in enumerate(ls):
            k,v = l
            if k == key:
                del self.arr[h][index]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)