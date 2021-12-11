class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def recursion(n, k, start=1, temp=[]):
            nonlocal result
            if k <= 0:
                result.append(list(temp))
                return temp
            for index in range(start, n+1):
                temp.append(index)
                # if (k-1) == 0:
                #     result.append(list(temp))
                t = recursion(n, k-1,index+1, temp)
                temp.pop()
        recursion(n,k,1,[])
        return result