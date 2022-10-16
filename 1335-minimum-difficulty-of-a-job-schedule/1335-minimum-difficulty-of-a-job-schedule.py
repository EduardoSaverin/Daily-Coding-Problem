class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        length = len(jobDifficulty)
        if length < d:
            return -1
        @lru_cache(None)
        def dfs(index, d):
            if d == 1:
                return max(jobDifficulty[index:])
            result, maxd = float("inf"), 0
            for i in range(index, length-d+1):
                maxd = max(maxd, jobDifficulty[i])
                result = min(result, maxd + dfs(i+1, d-1))
            return result
        return dfs(0, d)