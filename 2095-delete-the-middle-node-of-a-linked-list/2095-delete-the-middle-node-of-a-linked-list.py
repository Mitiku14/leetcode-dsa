# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dumy = ListNode(0)
        dumy.next = head
        prev = dumy
        n = 0
        while cur:
            n += 1
            cur = cur.next
        count = 0
        while count < n//2:
            prev = prev.next
            count += 1
        prev.next = prev.next.next
        return dumy.next


