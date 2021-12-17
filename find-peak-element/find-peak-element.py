class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        def findPeak(nums, low, high):
            if low > high:
                return -1
            mid= low+(high-low)//2
            if mid==0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            left = findPeak(nums, low, mid-1)
            if left == -1:
                return findPeak(nums, mid+1, high)
            return left
                
        return findPeak(nums, 0 ,len(nums)-1) 