class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dublicateFreeSet = set(nums)
        return len(dublicateFreeSet) != len(nums)