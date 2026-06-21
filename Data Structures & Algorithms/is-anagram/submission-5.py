class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode = 1.0
        for c in s:
            unicode = unicode * ord(c)
        for c in t:
            unicode = unicode / ord(c)
        return unicode == 1.0