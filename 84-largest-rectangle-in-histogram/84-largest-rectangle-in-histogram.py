class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # This 0 helps in cases like [1,2,3,4,5]
        stack = [-1]
        result = 0
        for index in range(len(heights)):
            # If Current Height Less Than Top Height of Stack
            while heights[index] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # print('Height', h)
                w = index -1 - stack[-1]
                result = max(result, h*w)
            stack.append(index)
        return result