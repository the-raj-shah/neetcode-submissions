class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = 0
        i = j = 0
        hSet = {}
        l = 1
        while(j < len(s)):
            # print(hSet, i, j, l)
            if(hSet.get(s[j]) != None):
                # print('here')
                l = max(l, j - i)
                i = hSet.get(s[j]) + 1
                hSet[s[j]] = j
            else:
                hSet[s[j]] = j
            j +=1
        return l
