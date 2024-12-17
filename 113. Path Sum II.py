# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, curr_sum, curr_arr):
            if not root:
                return

            curr_sum += root.val
            curr_arr.append(root.val)

            if not root.left and not root.right and curr_sum == targetSum:
                result.append(list(curr_arr))

            dfs(root.left, curr_sum, curr_arr)
            dfs(root.right, curr_sum, curr_arr)

            curr_arr.pop()

        dfs(root, 0, [])
        return result