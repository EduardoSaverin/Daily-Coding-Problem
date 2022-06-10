class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: -1)
        lastIndex = 0
        length = 0
        for index, char in enumerate(list(s)):
            lastIndex = max(lastIndex, d[char]+1)
            length = max(length, (index - lastIndex + 1))
            d[char] = index
        return length