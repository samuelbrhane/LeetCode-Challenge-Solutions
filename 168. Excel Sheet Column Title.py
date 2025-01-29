class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            char = chr(ord("A") + offset)
            result = char + result

            columnNumber = (columnNumber - 1) // 26
        
        return result