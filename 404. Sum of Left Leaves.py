# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        result = 0

        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                if node.left and not node.left.left and not node.left.right:
                    result += node.left.val

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                    
        return result