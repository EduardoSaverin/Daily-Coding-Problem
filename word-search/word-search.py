class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # No Need to check for empty board since in contraints it is 1 minimum
        # Word to searc is also 1 minimum
        # Created visited matrix to not visit same node in dfs dual
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, visited, word, 0, i, j):
                    return True
        return False
        
    def dfs(self, board, visited, word, index, i ,j):
        if len(word) == index:
            # If we reach till this point it means we have matched all nodes till here
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or word[index] != board[i][j]:
            return False
        visited[i][j] = 1
        result = self.dfs(board, visited, word, index+1, i+1,j) or self.dfs(board, visited, word, index+1, i-1,j) or self.dfs(board, visited, word, index+1, i,j-1)  or self.dfs(board, visited, word, index+1, i,j+1) 
        # While self unit testing found that it will fail for 
        # [["A","S","C","E"],["S","F","C","S"],["A","D","E","E"]]
        # "ASFCCESEEDAS"
        # If below unvisit not done
        visited[i][j] = 0
        return result