class Solution:
    def isPalindrome(self, s: str) -> bool:
        fP = 0
        bP = len(s) - 1
        while fP <= bP:
            while fP < len(s) - 1 and not s[fP].isalnum():
                fP += 1
            while bP > 0 and not s[bP].isalnum():
                bP -= 1
            if s[fP].casefold() != s[bP].casefold():
                return False
            fP += 1
            bP -= 1
        return True