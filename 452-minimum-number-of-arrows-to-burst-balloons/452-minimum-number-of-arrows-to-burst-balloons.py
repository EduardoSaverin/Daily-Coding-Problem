class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        # print(points)
        common = []
        for point in points:
            if len(common) == 0:
                common.append(point)
                continue
            last = common[-1]
            if last[1] >= point[0]:
                temp = [max(point[0], last[0]), min(point[1], last[1])]
                if temp[0] <= last[0] or temp[1] <= last[1]:
                    common[-1] = temp
                else:
                    common.append(temp)
            else:
                common.append(point)
            # print('->', common)
        return len(common)