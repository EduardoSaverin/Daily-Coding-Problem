class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = -float("inf")
        result = 0
        for pile in piles:
            maximum = max(pile, maximum)
        left, right = 1, maximum
        while left <= right:
            mid = left + (right-left) // 2
            steps = self.checkIfValid(mid, piles, h)
            if steps != -1:
                result = steps
                right = mid -1
            else:
                left = mid + 1
        return result
    
    def checkIfValid(self, k, piles, h):
        total = 0
        for pile in piles:
            total += math.ceil(pile/k)
        return k if total <= h else -1
        