class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode = 1
        for c in s:
            print(c, ord(c))
            unicode = unicode * ord(c)
        print(unicode)
        for c in t:
            print(c, ord(c))
            unicode = unicode / ord(c)
        print(unicode)
        return unicode == 1