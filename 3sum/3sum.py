class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        length = len(nums)
        result = []
        for index, value in enumerate(nums):
            if index > 0 and nums[index-1] == value:
                continue
            left = index+1
            right = length-1
            while left < right:
                total = value + nums[left] + nums[right]
                if total == 0:
                    # We are done
                    result.append([nums[index],nums[left], nums[right]])
                    left += 1
                    # Find non repeating next index
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
                    