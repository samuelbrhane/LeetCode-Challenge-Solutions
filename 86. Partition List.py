# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy, right_dummy = ListNode(), ListNode()
        left = left_dummy
        right = right_dummy

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        left.next = right_dummy.next
        right.next = None

        return left_dummy.next