class Solution:
    def __init__(self):
        self.MOD = 1000000007
        
    def numTilings(self, n: int) -> int:
        d = {}
        d[1] = 1 # For n=1 Just one Solution
        d[2] = 2 # For n=2 2 ways exists
        d[3] = 5 # For n=3 5 ways as given in question example 1
        d[1.5] = 1 # We know this from Tromino tile
        result = self.countTiles(n, d)
        return result
    
    def countTiles(self, n:int, d):
        if n in d:
            return d[n]
        if n < 1:
            return 0
        count = 0
        if n%1 == 0:
            # This case means no half point tile coming out and it is full rectangle till now
            # Not Three Cases Are there
            # Case 1 : One Vertical Domino
            # Case 2 : 2 Horizontal Domino
            # Case 3 : One Tromino, Here we can multiply by 2 since we can place this in two ways. Notice -1.5 because tromino will occupy 1.5 space
            count = (self.countTiles(n-1, d) + self.countTiles(n-2, d) + 2*self.countTiles(n-1.5, d)) % self.MOD
        else:
            # Here we can apply either Case 1 or Case 3 (only one time because we have to fill 0.5 space also and that can be one in one way only) only
            count = (self.countTiles(n-1, d) + self.countTiles(n-1.5, d)) % self.MOD
        d[n] = count
        return count