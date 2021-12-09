class Solution:
    def __init__(self):
        self.visited = set()
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr):
            return False
        # print(start)
        self.visited.add(start)
        if arr[start] == 0:
            return True
        left = False
        right = False
        if (start-arr[start]) not in self.visited:
            left = self.canReach(arr, start - arr[start])
        if (start + arr[start]) not in self.visited:
            right = self.canReach(arr, start + arr[start])
        return left or right