# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque([root])
        result = []

        while dq:
            level = []

            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    level.append(node.val)

                    if node.left:
                        dq.append(node.left)

                    if node.right:
                        dq.append(node.right)

            if level:
                result.append(max(level))

        return result
        