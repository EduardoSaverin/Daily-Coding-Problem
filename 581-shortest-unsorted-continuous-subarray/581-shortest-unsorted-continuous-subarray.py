class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        left, right = len(nums), len(nums)
        for index, value in enumerate(nums):
            # Flag to decide whether to put value in stack or not
            flag = False
            # Check if stack top value if greater than this number
            if stack and stack[-1][1] > value:
                # Store top value of stack for later push
                top = stack[-1]
                # Keep popping values until we keep finding greater values from stack top
                while stack and stack[-1][1] > value:
                    new_left_index = stack.pop()[0]
                left = min(left, new_left_index)
                right = index + 1
                stack.append(top)
                flag = True
            # This flag prevents smaller values than stack top getting pushed into stack
            if not flag:
                stack.append([index, value])
        return right- left