class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"}
        result = []

        def backtrack(i, string):
            if len(string) == len(digits):
                result.append(string)
                return

            char_str = num_map[digits[i]]

            for char in char_str:
                backtrack(i + 1, string + char)

        backtrack(0, "")
        return result