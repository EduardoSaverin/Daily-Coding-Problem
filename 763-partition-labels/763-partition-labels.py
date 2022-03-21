class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Looks like we have first create intervals and then merge them
        d = {}
        for index, char in enumerate(list(s)):
            if char not in d:
                d[char] = [index, index]
            else:
                start, end = d[char]
                d[char] = [start, index]
        intervals = list(d.values())
        merged_intervals = self.merge(intervals)
        result = []
        for start, end in merged_intervals:
            result.append(end-start+1)
        return result
        
    # This stub is taken from PB 56. Merge Intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        # intervals = sorted(intervals, key=cmp_to_key(self.comparator))
        # print(intervals)
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
                