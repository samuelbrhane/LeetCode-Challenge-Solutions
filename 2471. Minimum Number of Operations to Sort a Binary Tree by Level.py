# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def get_swaps(level):
            swaps = 0
            sorted_level = sorted(level)
            hash_map = {num:idx for idx, num in enumerate(level)}

            for i in range(len(level)):
                if level[i] != sorted_level[i]:
                    swaps += 1

                    idx = hash_map[sorted_level[i]]
                    level[i], level[idx] = level[idx], level[i]
                    hash_map[level[i]] = i
                    hash_map[level[idx]] = idx

            return swaps

        dq = deque([root])
        result = 0
        while dq:
            level = []

            for i in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)
            
            result += get_swaps(level)

        return result