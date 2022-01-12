class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        minimum = nums[0]
        max_of_all = nums[0]
        nums.pop(0)
        for num in nums:
            temp = max(num, num*maximum, num*minimum)
            minimum = min(num , num*maximum, num*minimum)
            maximum = temp
            max_of_all = max(max_of_all, maximum)
        return max_of_all
            
        
        