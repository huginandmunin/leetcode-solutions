from p206_reverse_linked_list import Solution, ListNode


def test_solution1():
    solution = Solution()
    # Get input lists and convert to nodes
    input = [1,2,3,4,5]
    list_input = solution.list_to_nodes(input)
    expected = [5,4,3,2,1]
    # Get node output and convert back to list
    output = solution.reverseList(list_input)
    output = output.to_list()
    assert output==expected

def test_solution2():
    solution = Solution()
    # Get input lists and convert to nodes
    input = [1,2]
    list_input = solution.list_to_nodes(input)
    expected = [2,1]
    # Get node output and convert back to list
    output = solution.reverseList(list_input)
    output = output.to_list()
    assert output==expected

def test_solution3():
    solution = Solution()
    # Get input lists and convert to nodes
    input = []
    list_input = solution.list_to_nodes(input)
    expected = []
    # Get node output and convert back to list
    output = solution.reverseList(list_input)
    if output:
        output = output.to_list()
    else:
        output = []
    assert output==expected