"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedNodes = set()
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result = max(result, self.getArea(grid, visitedNodes, row, col))
        return result
                    
    def getArea(self, grid: List[List[int]], visitedNodes, row, col) -> int:
        key = str(row) + "-" + str(col)
        if not self.inLimit(grid, row, col) or grid[row][col] != 1 or key in visitedNodes:
            return 0
        visitedNodes.add(key)
        area = 1
        area += self.getArea(grid, visitedNodes, row+1, col)
        area += self.getArea(grid, visitedNodes, row-1, col)
        area += self.getArea(grid, visitedNodes, row, col+1)
        area += self.getArea(grid, visitedNodes, row, col-1)
        return area
        
    def inLimit(self,grid,row,col):
        rows = len(grid)
        cols = len(grid[0])
        if row < rows and col < cols and row >= 0 and col >=0:
            return True
        return False
                
        