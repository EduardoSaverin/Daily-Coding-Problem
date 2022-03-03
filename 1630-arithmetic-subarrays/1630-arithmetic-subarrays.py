class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for index in range(len(l)):
            result.append(self.checkArithmetic(nums[l[index]: r[index]+1]))
        return result
    
    def checkArithmetic(self, nums: List[int]) -> bool:
        nums.sort()
        for index in range(2, len(nums)):
            if nums[index] - nums[index-1]  == nums[index-1] - nums[index-2]:
                continue
            else:
                return False
        return True