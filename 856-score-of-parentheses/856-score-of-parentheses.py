class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        par = 0
        for index, char in enumerate(list(s)):
            if char == "(":
                par += 1
            else:
                par -= 1
                if s[index-1] == "(":
                    score += (1<<par)
        return score
            
        
                