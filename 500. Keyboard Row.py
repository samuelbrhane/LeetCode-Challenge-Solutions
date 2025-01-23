class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []

        for word in words:
            row_changed = False
            main_row = 0
            typed = True
            for char in word:
                row = 0
                if char.lower() in first_row:
                    row = 1
                elif char.lower() in second_row:
                    row = 2
                else:
                    row = 3

                if row != main_row:
                    if not row_changed:
                        main_row = row
                        row_changed = True
                    else:
                        typed = False
                        break

            if typed:
                result.append(word)

        return result


