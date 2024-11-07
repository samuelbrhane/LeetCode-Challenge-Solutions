class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
                
            stack.append(char)
        
        stack = stack[:len(stack) - k]
        result = "".join(stack).lstrip("0")
        return result if result else "0"
