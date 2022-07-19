class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [
            [1],
            [1,1],
            [1,2,1]
        ]
        if numRows <= 3:
            return arr[:numRows]
        for i in range(3, numRows):
            newRow = [1]
            for j in range(1, i):
                newRow.append(arr[i-1][j-1] + arr[i-1][j])
            newRow.append(1)
            arr.append(newRow)
        return arr