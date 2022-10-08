class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result_remain = float("inf")
        result = 0
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            left = index+1
            right = len(nums)-1
            while left < right:
                remain = (num + nums[left] + nums[right]) - target
                if abs(remain) < abs(result_remain):
                    result_remain = remain
                    result = num + nums[left] + nums[right]
                if remain < 0:
                    left += 1
                elif remain > 0:
                    right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result
        