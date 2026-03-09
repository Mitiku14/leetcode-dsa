# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                prev.next = prev.next.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next

        return dummy.next
            
