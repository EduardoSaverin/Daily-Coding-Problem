class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = self.findPivot(nums)
        return nums[pivot]
        
    def findPivot(self, nums):
        low = 0
        high = len(nums) - 1
        if low == high:
            return low
        elif nums[low] < nums[high]:
            return low
        while low <= high:
            mid = low +(high-low)//2
            if mid < high and nums[mid] > nums[mid+1]:
                return mid+1
            elif mid > low and nums[mid-1]>nums[mid]:
                return mid
            elif nums[mid] > nums[low]:
                low = mid+1
            else:
                high = mid-1
            