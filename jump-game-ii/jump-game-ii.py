class Solution:
    def jump(self, nums: List[int]) -> int:
        # Trying Simple Iterative Solution
        target = len(nums)-1
        start,end = 0,0
        maxJump = 0
        count = 0
        while end < target:
            count += 1
            for index in range(start, end+1):
                maxJump = max(maxJump, index + nums[index])
            if maxJump >= target:
                return count
            start = end+1
            end = maxJump
        return count
            