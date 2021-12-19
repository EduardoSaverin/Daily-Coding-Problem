class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        index1 = 0
        index2 = 0
        result = []
        while index1 < len(firstList) and index2 < len(secondList):
            interval = [max(firstList[index1][0], secondList[index2][0]), min(firstList[index1][1], secondList[index2][1])]
            if interval[0] <= interval[1]:
                result.append(interval)
            if firstList[index1][1] < secondList[index2][1]:
                index1 += 1
            else:
                index2 += 1
        return result