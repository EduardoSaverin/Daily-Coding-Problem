class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefix = matrix
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                prefix[i][j] += prefix[i][j-1]
        counter = collections.Counter()
        count = 0
        # We calculate the prefix sum by row thus to get submatrix sum
        # we use startColumn and endColumn window to sub matrix sum.
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                counter.clear()
                counter[0] = 1 # Simple denotion that sum == k
                s = 0
                for k in range(len(matrix)):
                    # Consider [j] as endColumn and [i-1] as startColumn
                    s += prefix[k][j] - (prefix[k][i-1] if i > 0 else 0)
                    count += counter[s - target]
                    counter[s] += 1
        return count