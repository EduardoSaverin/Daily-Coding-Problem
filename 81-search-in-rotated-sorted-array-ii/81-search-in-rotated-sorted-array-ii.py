class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot = self.pivot(nums, target)
        return False if pivot == -1 else True
    
    def pivot(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            while left < mid and nums[left] == nums[mid]:
                left += 1
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    print(mid, right)
                    right = mid - 1
        return -1