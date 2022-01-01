class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Solution using Longest Common Subsequence
        # You can compare this solution with that and it will look exactly same
        m = len(word1)
        n = len(word2)
        arr = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        common = arr[m][n]
        return m-common+n-common