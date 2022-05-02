class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            # Odd Number
            if nums[left] % 2 != 0:
                # Find even from right side
                while left < right and nums[right] % 2 != 0:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        return nums