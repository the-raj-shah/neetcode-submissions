class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = 0
        i = j = 0
        hSet = {}
        l = 0
        while(j < len(s)):
            if(hSet.get(s[j]) != None):
                l = max(l, j - i)
                i = hSet.get(s[j]) + 1
                hSet[s[j]] = j
            else:
                hSet[s[j]] = j
            j +=1
        return l
