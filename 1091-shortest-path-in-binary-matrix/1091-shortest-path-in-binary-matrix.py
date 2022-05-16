class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        if self.rows > 0 and self.cols > 0 and (grid[0][0] != 0 or grid[self.rows-1][self.cols-1]!=0):
            return -1
        self.visited = set()
        q = []
        distance = float('inf')
        q.append([0,0,1]) # index 0,0 with distance 1
        while q:
            row, col , dis = q.pop(0)
            if row == self.rows-1 and col == self.cols - 1:
                distance = min(distance, dis)
            for x,y in [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]:
                if self.isValid(row+x, col+y) and grid[row+x][col+y] == 0 :
                    self.visited.add((row+x, col+y))
                    q.append([row+x, col+y, dis+1])
        return -1 if distance == float("inf") else distance
    def isValid(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and (row, col) not in self.visited:
            return True
        return False