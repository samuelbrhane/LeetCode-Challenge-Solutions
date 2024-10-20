class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char == ")":
                sub_stack = []
                while stack and stack[-1] != "(":
                    sub_stack.append(stack.pop())

                stack.pop()

                operator = stack.pop()
                
                if operator == "!":
                    val = "t" if sub_stack[0] == "f" else "f"
                elif operator == "&":
                    val = "t" if all(x == "t" for x in sub_stack) else "f"
                else:
                    val = "t" if any(x == "t" for x in sub_stack) else "f"

                stack.append(val)

            elif char != ",":
                stack.append(char)

        return stack.pop() == "t"