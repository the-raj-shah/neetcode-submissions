class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hSet = {}
        for i,v in enumerate(nums):
            if hSet.get((target - v), -1) != -1 and hSet.get((target - v), -1) != i:
                return [hSet[target - v], i]
            hSet[v] = i