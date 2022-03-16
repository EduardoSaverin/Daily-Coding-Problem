class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_index = 0
        pop_index = 0
        while push_index < len(pushed) and pop_index < len(popped):
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            stack.append(pushed[push_index])
            push_index += 1
        while stack and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1
        return True if len(stack) == 0 else False
            