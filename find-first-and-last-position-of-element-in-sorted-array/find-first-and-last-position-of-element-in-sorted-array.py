class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minIndex = self.findMinIndex(nums, target)
        maxIndex = self.findMaxIndex(nums, target)
        return [minIndex,maxIndex]
    
    def findMinIndex(self, nums, target, index=-1):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def findMaxIndex(self, nums, target, index=-1):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index