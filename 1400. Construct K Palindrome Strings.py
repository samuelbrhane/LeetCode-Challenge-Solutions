class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
            
        char_counts = Counter(s)
        odd_count = 0

        for char,count in char_counts.items():
            if count % 2:
                odd_count += 1

        return odd_count <= k