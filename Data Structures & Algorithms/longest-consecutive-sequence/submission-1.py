class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = set()
        lowest:int = None if len(nums) == 0 else nums[0]
        for i in range(0, len(nums)):
            lowest = lowest if lowest < nums[i] else nums[i]
            hashMap.add(nums[i])
        count = 1
        while count <= len(nums):
            if (lowest + count) in hashMap:
                count += 1
            else:
                break
        return count