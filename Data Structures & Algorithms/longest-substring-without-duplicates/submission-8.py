class Solution:
    # copied
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = {}
        for r in range(len(s)):
            # print(seen, l, r, max_len)
            if s[r] in seen:
                l =max(seen[s[r]]+1,l)
            seen[s[r]] = r
            max_len = max(max_len,r-l+1) 
        return max_len 
