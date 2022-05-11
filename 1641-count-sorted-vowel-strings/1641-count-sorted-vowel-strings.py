class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1]*6] + [[0]*(6) for _ in range(n)]
        for i in range(1, n+1):
            for k in range(1,6):
                dp[i][k] = dp[i-1][k] + dp[i][k-1]
        print(dp)
        return dp[n][k]
    
    # TLE
    def countVowelStringsOld(self, n: int) -> int:
        vowels = ['a','e','i', 'o', 'u']
        def recursion(vowels, start, path, result):
            if len(path) == n:
                result.append(path[:])
                return
            for index in range(start, len(vowels)):
                path.append(vowels[index])
                # No index+1 since vowels can repeat
                recursion(vowels, index, path, result)
                path.pop()
        result = []
        recursion(vowels, 0, [], result)
        return len(result)