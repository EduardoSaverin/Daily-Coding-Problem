class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 4
        nums.sort(reverse=True)
        if total % 4 != 0:
            return False
        return self.dfs(nums, [target]*4, 0)
        
    def dfs(self, nums, target, index):
        if index == len(nums):
            return target[0] == 0 and target[1] == 0 and target[2] == 0 and target[3] == 0
        for i in range(4):
            if nums[index] > target[i]:
                continue
            target[i] -= nums[index]
            if self.dfs(nums, target, index+1):
                return True
            target[i] += nums[index]
        return False