class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.result = ""
        for index in range(len(s)):
            self.expandAround(s, index, index+1)
            self.expandAround(s, index, index)
        return self.result
    
    def expandAround(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        if (right - (left+1)) > len(self.result):
            self.result = string[left+1:right]