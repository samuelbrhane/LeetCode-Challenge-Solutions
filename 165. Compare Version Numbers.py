class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_arr = version1.split(".")
        version2_arr = version2.split(".")

        max_len = max(len(version1_arr), len(version2_arr))

        for i in range(max_len):
            version1_num = int(version1_arr[i]) if i < len(version1_arr) else 0
            version2_num = int(version2_arr[i]) if i < len(version2_arr) else 0

            if version1_num < version2_num:
                return -1
            elif version1_num > version2_num:
                return 1

        return 0