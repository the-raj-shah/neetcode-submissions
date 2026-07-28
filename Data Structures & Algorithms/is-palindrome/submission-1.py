class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum())
        print(clean_text)
        fP = 0
        bP = len(clean_text) - 1
        while fP <= bP:
            if clean_text[fP].casefold() != clean_text[bP].casefold():
                return False
            fP += 1
            bP -= 1
        return True