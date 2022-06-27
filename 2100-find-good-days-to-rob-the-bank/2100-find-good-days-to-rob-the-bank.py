class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        decreasing = [1]
        count = 1
        for index in range(1, len(security)):
            if security[index-1] >= security[index]:
                count += 1
            else:
                count = 1
            decreasing.append(count)
        
        increasing = [1]
        count = 1
        for index in range(len(security)-2, -1, -1):
            if security[index+1] >= security[index]:
                count += 1
            else:
                count = 1
            increasing.append(count)
        increasing = increasing[::-1]
        indexes = []
        for index in range(len(security)):
            if decreasing[index] >= (time+1) and increasing[index] >= (time+1):
                indexes.append(index)
        return indexes
            