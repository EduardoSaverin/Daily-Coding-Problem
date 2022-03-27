class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for index in range(len(mat)):
            count = sum(mat[index])
            arr.append([count, index])
        arr = sorted(arr, key=cmp_to_key(Solution.compare))
        arr = arr[:k]
        result = []
        for count, index in arr:
            result.append(index)
        return result
            
    def compare(x,y):
        if x[0] == y[0]:
            return x[1] - y[1]
        return x[0] - y[0]