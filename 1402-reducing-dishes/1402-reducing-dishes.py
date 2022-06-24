class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        length = len(satisfaction)
        result = 0
        dp = [[0]*(length+1) for _ in range(length)]
        for i in range(length):
            for j in range(i+1, length+1):
                dp[i][j] = dp[i][j-1] + (j-i)*satisfaction[j-1]
                result = max(result, dp[i][j])
        # print(dp)
        return result