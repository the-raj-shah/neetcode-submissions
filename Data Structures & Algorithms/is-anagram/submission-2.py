class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode = 0.0
        for c in s:
            print(c, ord(c))
            unicode *= ord(c)
        for c in t:
            print(c, ord(c))
            unicode /= ord(c)
        return unicode == 0.0