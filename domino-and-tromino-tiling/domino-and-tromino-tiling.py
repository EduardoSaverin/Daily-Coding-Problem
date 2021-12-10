class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,2,5] + [0]*n
        for index in range(3, n):
            dp[index] = (dp[index-1]*2 + dp[index-3]) % 1000000007
        return dp[n-1]
# based on this explanation : https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1620809/PythonJAVACC%2B%2B-DP-oror-Visualized-Explanation-oror-100-Faster-oror-O(N)