class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        string1 = self.typing(s)
        string2 = self.typing(t)
        return string1 == string2
    
    def typing(self, s: str) -> str:
        stack = []
        for char in list(s):
            if char == '#' and stack:
                stack.pop()
            elif char != '#':
                stack.append(char)
        return ''.join(stack)