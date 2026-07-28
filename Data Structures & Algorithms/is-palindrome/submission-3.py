class Solution:
    def isPalindrome(self, s: str) -> bool:
        fP = 0
        bP = len(s) - 1
        while fP <= bP:
            while not s[fP].isalnum() and fP < len(s):
                fP += 1
            while not s[bP].isalnum() and bP > 0:
                bP -= 1
            if s[fP].casefold() != s[bP].casefold():
                return False
            fP += 1
            bP -= 1
        return True