from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_str(self):
        """ No comma before first item, print comma before remaining items """
        str = "["
        if self is not None and self.val is not None:
            l = self
            str += f"{l.val}"
            l = l.next
            while l:
                str += f",{l.val}"
                l = l.next
        str += "]"
        return str


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        lo = nout = ListNode(None)
        if head is None or head.next is None:
            return head

        lo.next = head
        lo = lo.next
        head = head.next
        while head:

            if lo.val < head.val:
                lo.next = head
                lo = lo.next

            head = head.next

        lo.next = None
        
        return nout.next


    def list_to_nodes(self, list):
        if not list:
            return None               
        ln = first_node = ListNode(None)
        for item in list:
            n = ListNode(item)
            ln.next = n
            ln = ln.next
        ln.next = None
        return first_node.next

