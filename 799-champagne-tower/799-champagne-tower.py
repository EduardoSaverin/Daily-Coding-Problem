class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0 for _ in range(row)] for row in range(1, query_row+2)]
        dp[0][0] = poured # Put All champagne at top
        for row in range(query_row):
            for col in range(len(dp[row])):
                if dp[row][col] > 1:
                    # (row+1) is the row just below current one
                    dp[row+1][col] += (dp[row][col]-1)/2.0
                    dp[row+1][col+1] += (dp[row][col]-1)/ 2.0
        return 1 if dp[query_row][query_glass] > 1 else dp[query_row][query_glass]