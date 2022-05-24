class Solution:
    def longestValidParentheses(self, s: str) -> int:
        self.length = 0
        left, right = 0, 0
        for char in list(s):
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                self.length = max(self.length, 2*left)
            elif right > left:
                left, right = 0,0
                
        left, right = 0, 0
        for char in list(s[::-1]):
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                self.length = max(self.length, 2*left)
            elif left > right:
                left, right = 0,0
        return self.length
        
    
    