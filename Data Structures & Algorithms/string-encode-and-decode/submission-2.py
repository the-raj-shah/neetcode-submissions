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
            while s[i] != '#':
                i += 1
            length = int(s[j:i])
            i +=1
            output.append(s[i:i+ length])
            i += length
        return output

