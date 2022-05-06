class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in list(s):
            if stack and stack[-1][0] == char:
                if stack[-1][1] == (k-1):
                    stack.pop()
                    # print('AFTER POP', stack)
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])
            # print('ITER', stack)
        result = ""
        for char, count in stack:
            result += char*count
        return result
        