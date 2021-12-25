class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        l = [1,2,3,4,5,6,7,8,9]
        def recursion(l, k ,start, n, path):
            if len(path) > k:
                return
            if  sum(path) == n and len(path) == k:
                result.append(path[:])
                return
            for index in range(start, len(l)):
                if index > start and l[index] == l[index-1]:
                    continue
                num = l[index]
                path.append(num)
                recursion(l, k, index+1, n, path)
                path.pop()
        recursion(l, k, 0, n, [])
        return result