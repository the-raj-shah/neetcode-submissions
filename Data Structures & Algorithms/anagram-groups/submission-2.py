class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputA = []
        sortHashSet = {}
        if len(strs) == 1:
            return [strs]
        for eachStr in strs:
            sortedString = "".join(sorted(eachStr)) 
            if sortedString in sortHashSet:
                outputA[sortHashSet[sortedString]].append(eachStr)
            else:
                outputA.append([eachStr])
                sortHashSet[sortedString] = len(outputA) - 1
        return outputA