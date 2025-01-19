class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        result = ""
        increment = (numRows - 1) * 2

        for row in range(numRows):
            for i in range(row, len(s), increment):
                result += s[i]

                zig_mid = (i + increment) - (2 * row)
                if 0 < row < numRows - 1 and zig_mid < len(s):
                    result += s[zig_mid]

        return result