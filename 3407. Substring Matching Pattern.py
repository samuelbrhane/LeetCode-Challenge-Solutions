class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        star_idx = p.index("*")
      
        prefix_idx = s.find(p[:star_idx])
        if prefix_idx == -1:
            return False

        suffix_idx = s[prefix_idx + star_idx:].find(p[star_idx + 1:])
        if suffix_idx == -1:
            return False

        return True