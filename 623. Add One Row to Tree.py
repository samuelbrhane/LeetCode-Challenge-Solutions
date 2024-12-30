# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left = root)

        def dfs(node, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                node.left = TreeNode(val, left = node.left)
                node.right = TreeNode(val, right = node.right)
            else:
                dfs(node.left, curr_depth + 1)
                dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root