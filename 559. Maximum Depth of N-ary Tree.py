"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            
            max_child_depth = 0
            if node.children:
                for child in node.children:
                    max_child_depth = max(max_child_depth, dfs(child))

            return max_child_depth + 1

        return dfs(root)