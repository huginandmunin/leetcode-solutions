from typing import List, Optional

# Definition for singly-linked list.
# eg, l1=ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
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


    def to_list(self):
        """ Helper method for unit tests """
        node_list = []
        if self is not None and self.val is not None:
            l = self
            node_list.append(l.val)
            l = l.next
            while l:
                node_list.append(l.val)
                l = l.next
        return node_list       


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Merge two sorted linked lists and return it as a sorted list. 
            The list should be made by splicing together the nodes of the first two lists.
            This solution iterates over nodes in both lists and compares values.
        """
        lo = nout1 = ListNode(None)
        if l1 is None and l2 is None:
            return lo

        while l1 and l2:
            if l1.val <= l2.val:
                lo.next = l1
                l1 = l1.next
            else:
                lo.next = l2
                l2 = l2.next
            lo = lo.next

        # Pick up remaining items
        while l1:
            lo.next = l1
            l1 = l1.next
            lo = lo.next

        while l2:
            lo.next = l2
            l2 = l2.next
            lo = lo.next

        return nout1.next      


    def list_to_nodes(self, list):
        """ Helper method for unit tests """
        if not list:
            return None               
        ln = first_node = ListNode(None)
        for item in list:
            n = ListNode(item)
            ln.next = n
            ln = ln.next
        ln.next = None
        return first_node.next
