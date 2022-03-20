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
    
    
    def minDominoRotationsOld(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        sorted_top_counter, top_counter = self.get_best(tops)
        sorted_bottom_counter, bottom_counter = self.get_best(bottoms)
        
        top_diff = float("inf")
        for key, count in sorted_top_counter:
            if total - count < top_diff and (count + bottom_counter[key] >= total) and self.valid(tops, bottoms, key):
                top_diff = total - count
                
        for key, count in sorted_bottom_counter:
            if total - count < top_diff and (count + top_counter[key] >= total) and self.valid(tops, bottoms, key):
                top_diff = total - count
        minimum = top_diff
        return -1 if minimum == float("inf") else minimum
            
    # Check if there exists position for a key in either top or bottom row
    def valid(self, tops, bottoms, key):
        for index in range(len(tops)):
            if key != tops[index] and key != bottoms[index]:
                return False
        return True
        
    # Return counter of keys
    def get_best(self, tops: List[int]):
        top_counter = Counter()
        for top in tops:
            top_counter[top] += 1
        return top_counter.most_common(), top_counter
