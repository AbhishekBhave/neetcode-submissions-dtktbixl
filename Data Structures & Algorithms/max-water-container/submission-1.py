class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            vol = height * (r - l)
            if vol > maximum:
                maximum = vol
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maximum
                    