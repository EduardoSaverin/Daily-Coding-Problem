class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Can be done using Patience Sort PB300
        envelopes.sort(key= lambda x : (x[0], -x[1]))
        piles = []
        for _, height in envelopes:
            left, right = 0, len(piles)
            while left < right:
                mid = (right + left) // 2
                if piles[mid] >= height:
                    right = mid
                else:
                    left = mid + 1
            if left == len(piles):
                piles.append(height)
            else:
                piles[left] = height
        return len(piles)
            