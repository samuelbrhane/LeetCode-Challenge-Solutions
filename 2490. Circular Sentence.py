class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        start_char = sentence[0]
        last_char = sentence[-1]
        
        if start_char != last_char:
            return False

        words = sentence.split()
        prev_end = words[0][-1]

        for i in range(1, len(words)):
            if prev_end != words[i][0]:
                return False
            prev_end = words[i][-1]
       
        return True