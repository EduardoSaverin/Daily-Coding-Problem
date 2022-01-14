class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest = -1
        secondhighest = -1
        max_index = -1
        for index, val in enumerate(nums):
            if val >= highest:
                secondhighest = highest
                highest = val
                max_index = index
            elif val > secondhighest:
                secondhighest = val
        if highest < 2*secondhighest:
            return -1
        return max_index