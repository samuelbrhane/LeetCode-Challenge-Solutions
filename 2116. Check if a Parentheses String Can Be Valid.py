class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(locked)
        if n % 2:
            return False

        stack_free = []
        stack_locked = []
        for i in range(n):
            if locked[i] == "0":
                stack_free.append(i)
            elif s[i] == "(":
                stack_locked.append(i)
            else:
                if stack_locked:
                    stack_locked.pop()
                elif stack_free:
                    stack_free.pop()
                else:
                    return False

        while stack_free and stack_locked and stack_locked[-1] < stack_free[-1]:
            stack_free.pop()
            stack_locked.pop()
        
        return False if stack_locked else True