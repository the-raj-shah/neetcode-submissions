class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hSet = {}
        for str in strs:
            count = tuple(sorted(Counter(str).items()))
            existingArray = hSet.get(count, [])
            existingArray.append(str)
            hSet[count] = existingArray
        return list(hSet.values())

    