# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque()
        dq.append(root)
        i = 0

        while dq:
            if i % 2:
                left, right = 0, len(dq) - 1
                while left < right:
                    dq[left].val, dq[right].val = dq[right].val, dq[left].val
                    left += 1
                    right -= 1
         
            for _ in range(len(dq)):
                node = dq.popleft()
                
                if node.left:
                    dq.append(node.left)
                if  node.right:
                    dq.append(node.right)

            i += 1
            
        return root