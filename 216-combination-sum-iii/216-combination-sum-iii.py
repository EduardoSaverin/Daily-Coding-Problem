class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l = [1,2,3,4,5,6,7,8,9]
        def recursion(l, start, path, result):
            if len(path) == k and sum(path) == n:
                result.append(path[:])
            for index in range(start, len(l)):
                if sum(path) + l[index] > n:
                    return
                recursion(l, index+1, path + [l[index]], result)
        result = []
        recursion(l,0,[], result)
        return result