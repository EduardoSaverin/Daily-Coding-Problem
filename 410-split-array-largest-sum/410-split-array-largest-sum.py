class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums) # 10
        high = sum(nums) # 32
        result = -1
        while low <= high:
            mid = (high+low)//2 # 21
            if self.valid_splits(nums, mid, m):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
    
    def valid_splits(self, nums, mid, m):
        count = 0
        current = 0
        for num in nums:
            if num + current > mid:
                current = 0
                count += 1
            current += num
        return count < m