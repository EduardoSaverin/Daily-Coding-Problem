class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Pattern s1 s2 s3
        s3 = -float("inf")
        # Stack contains all s2
        stack = []
        for index in range(len(nums)-1, -1, -1):
            # This Condition denotes that we have found all 3 elements
            if nums[index] < s3:
                return True
            while stack and stack[-1] < nums[index]:
                s3 = stack.pop()
            stack.append(nums[index])
        return False
                