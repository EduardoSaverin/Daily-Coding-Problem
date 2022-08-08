class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Patience Algorithm
        decks = [0]*len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left < right:
                mid = (right + left) // 2
                if decks[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            decks[left] = num
            size = max(left+1, size)
        return size