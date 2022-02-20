class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[0], x[0] - x[1]))
        # print(intervals)
        index = 0
        removing_index = []
        while index < len(intervals):
            x,y = intervals[index]
            while index+1 < len(intervals) and x <= intervals[index+1][0] and y >= intervals[index+1][1]:
                removing_index.append(index+1)
                index += 1
            index += 1
        # print(removing_index)
        return len(intervals) - len(removing_index)