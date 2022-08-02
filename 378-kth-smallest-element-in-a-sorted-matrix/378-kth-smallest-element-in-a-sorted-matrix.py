class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                h.append(matrix[i][j])
        heapq.heapify(h)
        k -= 1
        while k:
            heapq.heappop(h)
            k -= 1
        return heapq.heappop(h)