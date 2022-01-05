from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                count = 0
                for k in range(len(points)):
                    count += self.check_line(points[i], points[j], points[k])
                result = max(result, count)
        return 1 if result == 0 else result
                    
    def check_line(self, p1, p2, p3):
        if (p1[0]- p3[0])*(p2[1]-p3[1]) == (p1[1]- p3[1])*(p2[0]- p3[0]):
            return 1
        else:
            return 0
                    