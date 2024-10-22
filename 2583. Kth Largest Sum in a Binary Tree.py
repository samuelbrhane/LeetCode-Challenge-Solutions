# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        max_heap = []

        while q:
            level_sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heapq.heappush(max_heap, -level_sum)
        
        if k > len(max_heap):
            return -1
        
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        return -max_heap[0]
        