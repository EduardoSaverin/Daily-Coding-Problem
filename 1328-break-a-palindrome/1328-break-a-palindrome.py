class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        for index in range(length // 2):
            if palindrome[index] != 'a':
                return palindrome[:index] + 'a' + palindrome[index+1:]
        return palindrome[:-1] + "b" if length > 1 else ""