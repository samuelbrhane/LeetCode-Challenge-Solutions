# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def bfs(node, curr_str):
            if not node.left and not node.right:
                return result.append(curr_str)
            
            if node.left:
                left_str = f"{curr_str}->{node.left.val}"
                bfs(node.left, left_str)
                
            if node.right:
                right_str = f"{curr_str}->{node.right.val}"
                bfs(node.right, right_str)

        bfs(root, str(root.val))
        return result 