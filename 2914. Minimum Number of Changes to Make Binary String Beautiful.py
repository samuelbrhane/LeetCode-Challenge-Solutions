class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        char_list = list(s)

        for i in range(1, len(char_list)):
            if char_list[i] != char_list[i - 1] and i % 2 != 0:
                char_list[i] = char_list[i - 1]
                count += 1

        return count