class Solution:
    def canWinNim(self, n: int) -> bool:
        # In Game Theory Question always find one value of `n` 
        # for which player A will always loose. Then this value will
        # be used in all of the parts/questions.
        return (n%4) != 0