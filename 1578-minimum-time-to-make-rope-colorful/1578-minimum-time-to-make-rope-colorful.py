class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = None
        temp = []
        minTime = 0
        for i in range(len(colors)):
            this = colors[i]
            if prev is None or prev == this:
                temp.append(neededTime[i])
            elif prev != this:
                temp.sort()
                if len(temp) > 1:
                    minTime += sum(temp[:-1])
                temp = []
                temp.append(neededTime[i])
            prev = this
        if len(temp) > 1:
            temp.sort()
            minTime += sum(temp[:-1])
        return minTime
                