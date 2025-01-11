# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node, cur):
            if not node:
                return

            cur = chr(ord("a") + node.val) + cur
            if node.right and node.left:
                return min(
                    helper(node.right, cur),
                    helper(node.left, cur)
                )
            if node.right:
                return helper(node.right, cur)
            if node.left:
                return helper(node.left, cur)

            return cur

        return helper(root, "")