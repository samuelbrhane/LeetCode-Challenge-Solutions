# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree_set = self.bfs(root)

    def bfs(self, root):
        dq = deque([root])
        tree_set = set([0])
        root.val = 0

        while dq:
            node = dq.popleft()

            if node:
                if node.left:
                    node.left.val = 2 * node.val + 1
                    tree_set.add(node.left.val)
                    dq.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    tree_set.add(node.right.val)
                    dq.append(node.right)

        return tree_set


    def find(self, target: int) -> bool:
        return target in self.tree_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)