class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        length = len(nums)
        arr = [0]*len(nums)
        arr[0] = nums[0]
        arr[1] = nums[1]
        arr[2] = nums[0] + nums[2]
        for index in range(3, len(nums)):
            arr[index] = max(arr[index-3], arr[index-2]) + nums[index]
        return max(arr[length-1], arr[length-2])