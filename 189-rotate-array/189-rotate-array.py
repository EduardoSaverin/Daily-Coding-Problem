class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        
        # Revese Whole Array
        left = 0
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # Reverse first k elements
        left = 0
        right = k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # Reverse elements from k to end
        left = k
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1