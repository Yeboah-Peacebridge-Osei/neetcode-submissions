class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        left, right = 0, len(heights)-1
        while left < right:
            distance = right - left
            length = min(heights[left], heights[right])
            currentArea = length * distance
            result = max(currentArea, result)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result

        