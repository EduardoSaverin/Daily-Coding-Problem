class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        result = 1
        count = 1
        for letter in s[1:]:
            if letter == prev:
                count += 1
            else:
                result = max(result,count)
                count = 1
                prev = letter
        return max(result,count)