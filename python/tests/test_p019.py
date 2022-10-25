from p019_remove_nth_node_from_end_of_list import Solution, ListNode


def test_solution1():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [1,2,3,4,5]
    n = 2
    l1 = solution.list_to_nodes(input1)
    expected = [1,2,3,5]
    # Get node output and convert back to list
    output = solution.removeNthFromEnd(l1,n)
    output = output.to_list()
    assert output==expected

def test_solution2():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [1]
    n = 1
    l1 = solution.list_to_nodes(input1)
    expected = []
    # Get node output and convert back to list
    output = solution.removeNthFromEnd(l1,n)
    if output:
        output = output.to_list()
    else:
        output = []
    assert output==expected

def test_solution3():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [1,2]
    n = 1
    l1 = solution.list_to_nodes(input1)
    expected = [1]
    # Get node output and convert back to list
    output = solution.removeNthFromEnd(l1,n)
    output = output.to_list()
    assert output==expected