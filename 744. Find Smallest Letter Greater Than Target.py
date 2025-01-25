class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ord = ord(target)

        for char in letters:
            char_ord = ord(char)
            if char_ord > target_ord:
                return char

        return letters[0]