class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # n*(n+1)//2
        total_sum = (maxChoosableInteger+1) * maxChoosableInteger // 2
        if total_sum < desiredTotal:
            return False
        if total_sum == desiredTotal:
            return maxChoosableInteger % 2
        self.seen = {}
        choices = list(range(1, maxChoosableInteger+1))
        return self.recursion(choices, desiredTotal)
        
    def recursion(self, choices, remainder):
        # Since Choices is sorted and if last element of choice exceeds remainder 
        # then their is win
        if choices[-1] >= remainder:
            return True
        key = tuple(choices)
        if key in self.seen:
            return self.seen[key]
        for index in range(len(choices)):
            if not self.recursion(choices[:index] + choices[index+1:], remainder - choices[index]):
                self.seen[key] = True
                return True
        self.seen[key] = False
        return False
        