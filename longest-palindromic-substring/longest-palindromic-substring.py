class Solution:
    def __init__(self):
        self.word = ''
        self.length = 0
        
    def longestPalindrome(self, s: str) -> str:
        # I have done this question before also but will try to write cleaner solution this time.
        # Approach I will take here will be expanding around center of index until I find one non matching character
        for index in range(len(s)):
            self.expandAroundIndex(s, index, index) # For Odd Palindromic string
            self.expandAroundIndex(s, index, index+1) # For Even Palindromic string
        return self.word
        
    def expandAroundIndex(self, s, left , right):
        length = len(s)
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        if (right-(left+1)) > self.length:
            self.word = s[left+1:right]
            self.length = (right-(left+1)) # left + 1 <---- Because for left = -1 and right =3 it should be s[0:3]
            print(self.word)