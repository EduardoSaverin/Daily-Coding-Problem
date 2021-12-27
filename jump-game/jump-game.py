class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        maxJump = 0
        index = 0
        # If Current Index goes greater than maxJump (totally done till now) so far break the loop
        while index <= maxJump:
            maxJump = max(index + nums[index], maxJump)
            if maxJump >= target:
                return True
            index += 1
        return False
        
            
        