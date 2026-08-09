class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, 1
        water = 0
        while r < len(height):
            sH = 0
            if(height[r] >= height[l]):
                l = r
                r += 1
            while(height[l] > height[r]):
                sH += height[r]
                r +=1
                if(r >= len(height)):
                    sH = 0
                    break
            if(r < len(height)):
                water += (min(height[r],height[l]) * (r - l - 1) - sH)
            # print(l,r,sH, water)
        return water