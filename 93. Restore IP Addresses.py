class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(i, path):
            if len(path) == 4:
                if i == len(s):
                    result.append(".".join(path[:]))
                return

            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j+1]
                if (j > i and s[i] == "0") or int(segment) > 255:
                    continue

                backtrack(j + 1, path + [segment]) 

        backtrack(0, [])
        return result