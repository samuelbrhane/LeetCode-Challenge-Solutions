# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        result_sum = []

        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result_sum.append(level_sum)

        q = deque([root])
        root.val = 0
        level = 1

        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                sibling_sum = 0

                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    node.left.val = result_sum[level] - sibling_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = result_sum[level] - sibling_sum
                    q.append(node.right)

            level += 1

        return root