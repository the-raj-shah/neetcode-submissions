class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preP = [1] * len(nums)
        print(preP)
        suffP = [1] * len(nums)
        for i in range(1, len(nums)):
            preP[i] = preP[i - 1] * nums[i-1]
        for j in range(len(nums) - 2, -1, -1):
            suffP[j] = suffP[j + 1] * nums[j+1]
        res = []
        for i in range(0, len(nums)):
            res.append(preP[i]*suffP[i])
        return res
            
