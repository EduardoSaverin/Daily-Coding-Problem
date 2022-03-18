class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        indexes = {}
        visited = set()
        for index, char in enumerate(list(s)):
            indexes[char] = index
        for index, char in enumerate(list(s)):
            if char not in visited:
                while stack and stack[-1] > char and index < indexes[stack[-1]]:
                    c = stack.pop()
                    visited.remove(c)
                stack.append(char)
                visited.add(char)
        return ''.join(stack)