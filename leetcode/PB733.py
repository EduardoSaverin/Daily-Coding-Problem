"""
Flood Fill
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
Return the modified image
"""
from typing import List

class Solution:
    def __init__(self):
        self.visitedNode = set()
        self.matchingColor = -1
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.matchingColor = image[sr][sc]
        self.markNodes(image,sr,sc,newColor)
        return image
    
    def markNodes(self, image, row, col, newColor):
        if not self.inLimit(image,row,col):
            return
        key = str(row) + "-" + str(col)
        if image[row][col] == self.matchingColor and  key not in self.visitedNode:
            self.visitedNode.add(key)
            image[row][col] = newColor
            self.markNodes(image, row+1, col, newColor)
            self.markNodes(image, row, col-1, newColor)
            self.markNodes(image, row, col+1, newColor)
            self.markNodes(image, row-1, col, newColor)
            
    def inLimit(self,image,row,col):
        rows = len(image)
        cols = len(image[0])
        if row < rows and col < cols and row >= 0 and col >=0:
            return True
        return False