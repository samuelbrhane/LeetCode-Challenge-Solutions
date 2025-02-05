class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        mismatch = []

        for i in range(n):
            if s1[i] != s2[i]:
                mismatch.append((s1[i], s2[i]))

        if len(mismatch) == 2:
            return mismatch[0] == mismatch[-1][::-1]

        return len(mismatch) == 0