class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode = 1.0
        for c in s:
            print(ord(c))
            unicode = unicode * (ord(c)- ord('a') + 1)
        print(unicode)
        for c in t:
            print(ord(c))
            unicode = unicode / (ord(c)- ord('a') + 1)
        print(unicode)
        return unicode == 1.0