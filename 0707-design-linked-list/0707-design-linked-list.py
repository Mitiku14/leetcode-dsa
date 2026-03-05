class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        cur = self.head
        pos = 0

        while cur and pos < index:
            cur = cur.next
            pos += 1

        if cur:
            return cur.val
        return -1


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        dummy = ListNode(0)
        dummy.next = self.head

        prev = dummy
        cur = self.head
        ind = 0

        while cur and ind < index:
            prev = cur
            cur = cur.next
            ind += 1

        if ind == index:
            new_node = ListNode(val)
            prev.next = new_node
            new_node.next = cur

        self.head = dummy.next


    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode(0)
        dummy.next = self.head

        prev = dummy
        cur = self.head
        ind = 0

        while cur and ind < index:
            prev = cur
            cur = cur.next
            ind += 1

        if cur and ind == index:
            prev.next = cur.next

        self.head = dummy.next