class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        return self.edit_distance(word1, word2, m ,n)
    @lru_cache()
    def edit_distance(self, word1, word2, m, n):
        if m == 0:
            return n
        if n == 0:
            return m
        if word1[m-1] == word2[n-1]:
            return self.edit_distance(word1, word2, m-1, n-1)
        return 1+min(self.edit_distance(word1, word2, m-1, n), self.edit_distance(word1, word2, m-1, n-1), self.edit_distance(word1, word2, m, n-1))