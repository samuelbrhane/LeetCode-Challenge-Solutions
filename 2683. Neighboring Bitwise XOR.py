class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first, last = 0, 0 

        for num in derived:
            if num:
                last = ~last

        return first == last