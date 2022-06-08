class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # minimum number of steps to make the given string empty -> it means it will always get empty
        # If already plaindrome remove in 1 step if not then remove 'a' in 1 step and then remove b in 2nd step
        # Hence max 2 steps
        return 1 if s == s[::-1] else 2