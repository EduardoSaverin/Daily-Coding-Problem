class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l = []
        row = len(grid)
        col = len(grid[0])
        total = row*col
        for i in range(len(grid)):
            for element in grid[i]:
                l.append(element)
        k = k % total
        l = l[-k:] + l[:(total-k)]
        left = 0
        right = col
        final = []
        while right <= total:
            # print(left, right)
            final.append(l[left: right])
            left = right
            right += col
        return final
                