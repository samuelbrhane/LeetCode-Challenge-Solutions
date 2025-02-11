class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                del stack[-part_len:]

        return "".join(stack)