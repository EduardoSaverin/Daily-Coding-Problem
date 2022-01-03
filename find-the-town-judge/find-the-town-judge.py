class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0]*n
        outDegree = [0]*n
        for a,b in trust:
            outDegree[a-1] += 1
            inDegree[b-1] += 1
        index = 0
        # print(inDegree)
        # print(outDegree)
        for degree in inDegree:
            if degree == (n-1):
                if outDegree[index] == 0:
                    return (index+1)
            index += 1
        return -1