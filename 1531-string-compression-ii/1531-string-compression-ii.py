class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {}
        def recursion(index, current, length, del_remain):
            if index == len(s):
                return 0
            key = (index, current, length, del_remain)
            if key in dp:
                return dp[key]
            
            # Delete Cost
            del_cost = float("inf")
            if del_remain > 0:
                del_cost = recursion(index+1, current, length, del_remain-1)
            
            # Keep Char Cost
            keep_cost = 0
            if s[index] == current:
                extra_cost = 0
                if length == 1 or len(str(length+1)) > len(str(length)):
                    extra_cost = 1
                keep_cost = extra_cost + recursion(index+1, current, length+1, del_remain)
            else:
                keep_cost = 1 + recursion(index+1, s[index], 1, del_remain)
            
            dp[key] = min(del_cost, keep_cost)
            return dp[key]
        return recursion(0, '', 0, k)