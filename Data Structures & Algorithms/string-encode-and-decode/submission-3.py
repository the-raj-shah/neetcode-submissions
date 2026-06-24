class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            j = index

            while s[j] != '#':
                j += 1
            
            length = int(s[index:j])
            index = j + 1
            res.append(s[index: index + length])
            
            index += length
        
        return res


