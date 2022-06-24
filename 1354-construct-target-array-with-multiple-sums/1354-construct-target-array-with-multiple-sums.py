class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Pick Largest element from given array
        # Subtract from sum of rest of the elements
        # Keep doing this until all one
        total = sum(target)
        arr = [-num for num in target]
        heapify(arr) # Created Max Heap using negative value
        while True:
            val = -heappop(arr)
            total -= val
            if val == 1 or total == 1:
                return True
            if val < total or total == 0 or val % total == 0:
                return False
            val %= total
            total += val
            heappush(arr, -val)