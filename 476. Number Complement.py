class Solution:
    def findComplement(self, num: int) -> int:
        bit = format(num, 'b')
        result = []

        for char in bit:
            flip = "1" if char == "0" else "0"
            result.append(flip)

        return int("".join(result), 2)