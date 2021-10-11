from typing import Optional

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Start with the least significant digits, which are at 
            the beginning of the reversed lists.
            Carry as needed.
        """
        sum = 0
        carry = 0
        lo = nout = ListNode(None)
       
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                sum = sum %10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sum)
            lo.next = new_node

            lo = lo.next
            l1 = l1.next
            l2 = l2.next

        # Pick up remaining items
        while l1:
            sum = l1.val + carry
            if sum >= 10:
                sum = sum %10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sum)
            lo.next = new_node
            l1 = l1.next
            lo = lo.next

        while l2:
            sum = l2.val + carry
            if sum >= 10:
                sum = sum %10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(sum)
            lo.next = new_node
            l2 = l2.next
            lo = lo.next
            
        if carry:
            new_node = ListNode(carry)
            lo.next = new_node
            lo = lo.next

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

