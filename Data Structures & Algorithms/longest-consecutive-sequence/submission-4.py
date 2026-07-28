class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valuesSet = set(nums)
        l = 0
        for num in nums:
            subCount = 0
            while num + subCount in valuesSet:
                subCount += 1
            if (subCount > l):
                l = subCount
        return l