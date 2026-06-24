class Solution:
# watched video first
    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        for s in strs:
            outputStr += (str(len(s)) + "#" + s)
        return outputStr
    def decode(self, s: str) -> List[str]:
        outList = []
        num = 0
        tempString = ""
        for i in s:
            print(i)
            if i == "#":
                num = int(tempString)
                tempString = ""
            else:
                tempString += i
                num -= 1
                if num == 0:
                    outList.append(tempString)
                    tempString = ""
            print(tempString, num)
        print(outList)
        if len(outList) == 0:
            return [""]
        return outList