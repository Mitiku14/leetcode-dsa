# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        seen = set()
        while cur:
            seen.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in seen:
                return cur
            cur = cur.next
        return None