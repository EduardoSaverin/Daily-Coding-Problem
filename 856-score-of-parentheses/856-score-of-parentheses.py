class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for index, char in enumerate(list(s)):
            if char == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score*2, 1)
        return score
            
        
                