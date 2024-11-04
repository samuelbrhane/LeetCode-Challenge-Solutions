class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        char_added = set()

        for i, char in enumerate(s):
            if char in char_added:
                continue

            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                char_added.remove(removed_char)

            stack.append(char)
            char_added.add(char)
        
        return "".join(stack)

        