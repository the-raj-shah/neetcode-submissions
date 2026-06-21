class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode = 1.0
        for c in s:
            unicode = unicode * (ord(c)- ord('a') + 1)
        for c in t:
            unicode = unicode / (ord(c)- ord('a') + 1)
        return unicode == 1.0