class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - max(salary) - min(salary)
        n = len(salary) - 2
        return total / n
