class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = -1
        maximum = -1
        for index, val in enumerate(nums):
            if val > maximum:
                max_index = index
                maximum = val
        if max_index == -1:
            return -1
        for index, val in enumerate(nums):
            if index == max_index:
                continue
            elif maximum < 2*val:
                return -1
        return max_index