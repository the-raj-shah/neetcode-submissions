class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formala = (x2-x1)*min(y1,y2)
        l,r = 0, len(heights) - 1
        mv = 0
        while l < r:
            v = (r - l) * min(heights[l], heights[r])
            if v > mv:
                mv = v
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return mv