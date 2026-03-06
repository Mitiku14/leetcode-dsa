# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0
        ans = head
        while cur:
            n += 1
            cur = cur.next
        count = 0
        while count < n //2:
            count += 1
            ans = ans.next
        return ans



        
