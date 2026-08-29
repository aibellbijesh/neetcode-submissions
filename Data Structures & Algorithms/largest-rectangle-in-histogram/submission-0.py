class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for r, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                i = stack.pop()
                h = heights[i]
                if stack:
                    w = r - stack[-1] - 1
                else:
                    w = r
                max_area = max(max_area, h * w)
            stack.append(r)
        return max_area