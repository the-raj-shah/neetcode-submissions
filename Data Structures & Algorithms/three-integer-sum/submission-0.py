class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        out = []
        for i,num in enumerate(sortedNums):
            fp,bp = i+1,len(sortedNums) - 1
            if num != sortedNums[i - 1]:
                while fp < bp:
                    if sortedNums[fp] + sortedNums[bp] == 0 - num:
                        out.append([sortedNums[fp], sortedNums[bp], num])
                        fp += 1
                        bp -= 1
                    elif sortedNums[fp] + sortedNums[bp] < 0 - num:
                        fp += 1
                    else:
                        bp -= 1
        return out
