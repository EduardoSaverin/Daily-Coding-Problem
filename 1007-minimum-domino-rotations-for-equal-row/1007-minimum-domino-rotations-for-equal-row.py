class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        same, countA, countB = Counter(), Counter(A), Counter(B)
        for a, b in zip(A, B):
            if a == b:
                same[a] += 1
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                # countA-same or countB-same since `same` is common here take min of two counts
                return min(countA[i], countB[i]) - same[i]        
        return -1