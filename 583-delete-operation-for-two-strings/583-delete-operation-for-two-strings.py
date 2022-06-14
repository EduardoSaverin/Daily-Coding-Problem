class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = 1 + d[i-1][j-1]
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        return len(word1) + len(word2) - 2*d[-1][-1]