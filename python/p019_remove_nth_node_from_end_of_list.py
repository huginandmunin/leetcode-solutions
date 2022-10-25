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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        Traverse list to get count of items in list. 
        Make another pass to remove nth from end.
        """
        if n == 0:
            return head
        if not head.next:
            # return empty list
            return None

        # one pass to count items in last
        i = 1
        prev = head
        while prev.next:
            prev = prev.next
            i += 1
        count = i

        # handle case of n == length: delete head
        if count==n:
            head = head.next
            return head

        # handle case of deleting last item  
        if count+1-n==1:
            prev.next = None
            return head

        # another pass to get to node to delete
        prev = head
        current = head.next
        for i in range(2,count+1-n):
            prev = current
            current = current.next
        if current.next:
            prev.next = current.next
        else:
            prev.next = None

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


if __name__ == "__main__":
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [1,2]
    n = 2
    l1 = solution.list_to_nodes(input1)
    expected = [2]
    # Get node output and convert back to list
    output = solution.removeNthFromEnd(l1,n)
    if output:
        output = output.to_list()
        print(f"output = {output}")
    else:
        output = []
    assert output==expected
