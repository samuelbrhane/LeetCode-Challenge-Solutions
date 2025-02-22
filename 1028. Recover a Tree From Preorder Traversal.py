# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        stack = []

        while i < len(traversal):
            level, val = 0, 0

            while i < len(traversal) and traversal[i] == "-":
                level += 1
                i += 1

            j = i
            while j < len(traversal) and traversal[j] != "-":
                j += 1
            val = int(traversal[i:j]) 

            node = TreeNode(val)

            while len(stack) > level:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)
            i = j  

        return stack[0] 