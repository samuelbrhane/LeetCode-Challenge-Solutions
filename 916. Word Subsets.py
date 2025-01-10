class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char in word_freq:
                max_freq[char] = max(max_freq[char], word_freq[char])

        for word in words1:
            word_freq = Counter(word)
            word_subset = True
            for char in max_freq:
                if word_freq[char] < max_freq[char]:
                    word_subset = False
                    break
                    
            if word_subset:
                result.append(word)
        
        return result