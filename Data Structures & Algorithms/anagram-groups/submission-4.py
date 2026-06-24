class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hSet = {}
        for str in strs:
            counter = [0] * 26
            for s in str:
                counter[ord(s) - ord('a')] += 1
            count = tuple(counter)
            existingArray = hSet.get(count, [])
            existingArray.append(str)
            hSet[count] = existingArray
        return list(hSet.values())

    