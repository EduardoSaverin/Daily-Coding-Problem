class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        distance = [[None]*col for _ in range(row)]
        dq = deque()
        for i in range(row):
            for j in range(col):
                if not mat[i][j]:
                    distance[i][j] = 0 # Putting All Zeroes first and then visit its adjacent
                    dq.append((i,j))
        while dq:
            i,j = dq.popleft()
            # This None Check in All is to check if it has not been visited yet
            if (i-1) >= 0 and distance[i-1][j] is None:
                distance[i-1][j] = distance[i][j] + 1
                dq.append((i-1,j)) # Now push it so that we can visit its adjacent ones
            if (j-1) >= 0 and distance[i][j-1] is None:
                distance[i][j-1] = distance[i][j] + 1
                dq.append((i,j-1)) # Now push it so that we can visit its adjacent ones
            if (i+1) < row and distance[i+1][j] is None:
                distance[i+1][j] = distance[i][j] + 1
                dq.append((i+1,j)) # Now push it so that we can visit its adjacent ones
            if (j+1) < col and distance[i][j+1] is None:
                distance[i][j+1] = distance[i][j] + 1
                dq.append((i,j+1)) # Now push it so that we can visit its adjacent ones
        
        return distance