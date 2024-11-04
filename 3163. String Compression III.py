class Solution:
    def compressedString(self, word: str) -> str:
        curr_char = word[0]
        streak = 1
        result = ""

        for i in range(1, len(word)):
            if word[i] == curr_char and streak < 9:
                streak += 1
            else:
                result += f"{str(streak)}{curr_char}"
                curr_char = word[i]
                streak = 1
        
        return result + f"{str(streak)}{curr_char}"