class Solution:
# watched video first
    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        for s in strs:
            outputStr += (str(len(s)) + "#" + s)
        return outputStr
    def decode(self, s: str) -> List[str]:
        output, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            output.append(s[j+1:j+ length + 1])
            i = j + length + 1
        return output

