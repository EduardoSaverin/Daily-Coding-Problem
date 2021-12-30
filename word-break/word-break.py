class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # This is first time I'm using this @lru_cache
        @lru_cache(None)
        def recursion(index):
            if index >= len(s):
                return True
            for j in range(index, len(s)):
                substring = s[index:j+1]
                if substring in wordDict:
                    if recursion(j+1): # Think of this as `and` condition this substring and remaning word
                        return True
            return False
        return recursion(0)