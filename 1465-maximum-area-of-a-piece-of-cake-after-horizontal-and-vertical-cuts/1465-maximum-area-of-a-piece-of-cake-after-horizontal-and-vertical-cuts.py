class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        start_point = 0
        max_hor = 0
        for cut in sorted(horizontalCuts):
            length = cut - start_point
            max_hor = max(length, max_hor)
            start_point = cut
        # print(start_point, h)
        max_hor = max(h - start_point, max_hor)
        start_point = 0
        max_ver = 0
        for cut in sorted(verticalCuts):
            length = cut - start_point
            max_ver = max(length, max_ver)
            start_point = cut
        # print(start_point, w)
        max_ver = max(max_ver, w-start_point)
        return (max_hor*max_ver) % (10**9+7)
                