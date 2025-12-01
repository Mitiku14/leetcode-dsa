# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        n = len(res)
        for i in range(1, n):
            key = res[i]
            j = i - 1
            while j >= 0 and res[j] > key:
                res[j+1] = res[j]
                j -= 1
            res[j+1] = key
        dummy = ListNode(0)
        curr = dummy
        for value in res:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next
