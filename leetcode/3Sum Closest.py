# [LINK] https://leetcode.com/problems/3sum-closest/
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Results will be stored
        result_remain = float('inf')
        # Sort the number list : O(nlogn)
        nums.sort()
        length = len(nums)
        # Pick one value as a and other two will be picked using left and right pointers
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            left, right = index+1, length-1
            while left < right:
                remain = ((nums[left] + nums[right] + value) - target)
                if abs(remain) < abs(result_remain):
                    result_remain = remain
                    result = (value + nums[left] + nums[right])
                # if Value is less than 0 increment left since left values are small
                if remain < 0:
                    left += 1
                # if Value is greater than 0 decrement right since right values are large
                elif remain > 0:
                    right -= 1
                # Value is zero
                else:
                    
                    left += 1
                    # Since we don't want duplicate result in same iteration we keep right pointer unchanged 
                    # and increment left until it is not same as its left-side value
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result