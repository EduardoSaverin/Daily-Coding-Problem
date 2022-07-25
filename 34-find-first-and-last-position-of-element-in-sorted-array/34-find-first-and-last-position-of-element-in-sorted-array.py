class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        left = self.binary(True)
        if left == -1:
            return [-1,-1]
        right = self.binary()
        return [left, right]
        
    def binary(self, leftmost = False):
        target = self.target
        left = 0
        right = len(self.nums)
        index = -1
        while left < right:
            mid = left + (right-left) // 2
            if self.nums[mid] == target:
                index = mid
                if leftmost:
                    right = mid
                else:
                    left = mid + 1
            elif self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return index
        