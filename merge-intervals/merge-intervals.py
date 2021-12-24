class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            lastInterval = result[-1]
            thisTime = interval[0]
            lastTime = lastInterval[1]
            if thisTime <= lastTime:
                newInterval = [min(lastInterval[0], interval[0]), max(lastInterval[1], interval[1])]
                result.pop()
                result.append(newInterval)
            else:
                result.append(interval)
        return result
