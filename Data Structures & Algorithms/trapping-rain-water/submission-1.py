class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = maxR = water = 0
        l,r = 0, len(height) - 1
        while(l <= r):
            if(maxL < maxR):
                maxL = max(maxL, height[l])
                water += (maxL - height[l])
                l += 1
            else:
                maxR = max(maxR, height[r])
                water +=  (maxR - height[r])
                r -= 1
        return water
             