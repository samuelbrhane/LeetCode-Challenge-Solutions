class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_len = len(pattern)
        s_arr = s.split(" ")
        s_len = len(s_arr)

        if pat_len != s_len:
            return False

        word_char = {}
        char_word = {}
       
        for char, word in zip(pattern, s_arr):
            if char in char_word and char_word[char] != word:
                return False
            else:
                char_word[char] = word

            if word in word_char and word_char[word] != char:
                return False
            else:
                word_char[word] = char
   
        return True