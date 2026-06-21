class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = {}
        for c in s:
            hashSet[c] = hashSet.get(c, 0) + 1
        for c in t:
            if c in hashSet:
                hashSet[c] = hashSet[c] - 1
                if hashSet[c] == 0:
                    hashSet.pop(c)
        return len(hashSet) == 0