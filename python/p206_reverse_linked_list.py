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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative: starting at head, move next item to head."""

        if not head or not head.next:
            return head

        current = head
        while current.next:
            next_item = current.next
            current.next = next_item.next
            next_item.next = head
            head = next_item 
        return head       

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
