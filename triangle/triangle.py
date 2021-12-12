class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Move from Bottom to UP
        # For Second row from bottom update minimum in that row using its below row
        # Same goes for its upper rows
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                # For Row 2 Column 0 <--- Min(Row 3 Column 0, Row 3 Column 1)
                # In Same way do for other columns in same row, then ,move to upper row
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]