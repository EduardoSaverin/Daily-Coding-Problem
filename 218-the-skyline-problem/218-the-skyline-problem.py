class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Store all left and rights in set
        points = set()
        for left, right, height in buildings:
            points.add(left)
            points.add(right)
        points = list(points)
        # print(points)
        points.sort() # Sort
        # Pick each point
        result = [[-1,0]]
        index = 0
        towers = []
        for point in points:
            while index < len(buildings) and point >= buildings[index][0]:
                # This is first time I'm using python heaps :P, they are min-heaps by default that's why using -ve
                heappush(towers, (-buildings[index][2], buildings[index][1]))
                index += 1
            while towers and point >= towers[0][1]:
                heappop(towers)
            height = -towers[0][0] if towers else 0
            if height != result[-1][1]:
                result.append([point, height])
        return result[1:]
