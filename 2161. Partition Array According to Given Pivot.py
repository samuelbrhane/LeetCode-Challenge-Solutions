class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, piv, greater = [], [], []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                piv.append(num)

        return less + piv + greater
