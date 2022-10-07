class Node:
    def __init__(self, start, end, time=1):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.time = time
class MyCalendarThree:

    def __init__(self):
        self.root = None
        self.k = 0
        

    def book(self, start: int, end: int) -> int:
        self.root = self.helper(self.root, start, end, 1)
        return self.k
    
    def helper(self, root, start, end, time):
        if start >= end:
            return root
        if not root:
            self.k = max(self.k, time)
            return Node(start, end, time)
        else:
            if start >= root.end:
                root.right = self.helper(root.right, start, end, time)
            elif end <= root.start:    
                root.left = self.helper(root.left, start, end, time)
            else:
                a = min(root.start, start)
                b = max(root.start, start)
                c = min(root.end, end)
                d = max(root.end, end)
                
                root.left = self.helper(root.left, a, b, root.time if a == root.start else time)
                root.right = self.helper(root.right, c, d, root. time if d == root.end else time)
                
                root.time += time
                root.start = b
                root.end = c
                self.k = max(self.k, root.time)
            return root
                
                
        