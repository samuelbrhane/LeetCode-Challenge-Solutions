class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy_str = s[0:2]

        for i in range(2, len(s)):
            if s[i] != fancy_str[-1] or s[i] != fancy_str[-2]:
                fancy_str += s[i]

        return fancy_str