class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_content = 0

        for cookie_size in s:
            if child_content < len(g) and cookie_size >= g[child_content]:
                child_content += 1
        
        return child_content