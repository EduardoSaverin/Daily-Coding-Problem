class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dq = deque()
        time = 0
        fresh = set() # To Check if fresh is still there and fresh not updated twice
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    dq.append((i,j,0)) # Third thing is time Rotting orange has 0 time
        while dq:
            i,j,thistime = dq.popleft()
            time = max(time,thistime)
            for x,y in ((i-1,j), (i,j-1), (i+1,j), (i,j+1)):
                # not checking any boundary because we have already fresh indexes that we will check below
                if (x,y) in fresh:
                    dq.append((x,y,thistime+1))
                    fresh.remove((x,y))
        return -1 if fresh else time
        
                    