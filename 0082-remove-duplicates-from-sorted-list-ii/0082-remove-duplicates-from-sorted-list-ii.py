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
                duplicate = cur.val
                while cur and cur.val == duplicate:
                    cur = cur.next
                prev.next = cur
            
            else:
                prev = cur
                cur = cur.next
    
        return dummy.next