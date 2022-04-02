class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        count = 1 # Number of deletes
        return self.check_palindrome(s, left, right, count)
        
    def check_palindrome(self, string, left, right, count):
        while left < right:
            if string[left] != string[right]:
                if count <= 0 :
                    return False
                return self.check_palindrome(string, left+1, right, count-1) or self.check_palindrome(string, left, right-1, count-1)
            left += 1
            right -= 1
        return True
        