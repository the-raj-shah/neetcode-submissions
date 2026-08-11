class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = 0
        i = j = 0
        hSet = set()
        l = 0
        while(j < len(s)):
            if s[j] in hSet:
                l = max(l, j-i)
                while i < j:
                    hSet.discard(s[i])
                    i +=1
            hSet.add(s[j])
            j +=1
            # print(hSet, i, j)
        return max(l, j-i)
