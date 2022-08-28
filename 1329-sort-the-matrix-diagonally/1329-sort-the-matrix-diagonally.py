class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #.
        row, col = len(mat), len(mat[0])
        
        # This diagonal parse logic is important
        for i in range(1, row + col - 2):
            if i < row:
                start_row, start_col = row - i - 1, 0
            else:
                start_row, start_col = 0, i - row + 1
            
            # Add all diagonal elements to arr
            diag = []
            while start_row < row and start_col < col:
                diag.append(mat[start_row][start_col])
                start_row += 1
                start_col += 1
            # Sort array
            diag.sort()
            start_row -= 1
            start_col -= 1
            while start_row >= 0 and start_col >= 0:
                # Add back all sort diagonal elements back
                mat[start_row][start_col] = diag.pop()
                start_row -= 1
                start_col -= 1

        return(mat)