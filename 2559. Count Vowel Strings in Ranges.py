class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ["a", "e", "i", "o", "u"]
        result = []
        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
       
        for left, right in queries:
            vowel_sum = prefix[right + 1] - prefix[left]
            result.append(vowel_sum)

        return result
        