from p021_merge_two_sorted_lists import Solution, ListNode


def test_solution1():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [1,2,4]
    input2 = [1,3,4]
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = [1,1,2,3,4,4]
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected

def test_solution2():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = []
    input2 = []
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = []
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected

def test_solution3():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = []
    input2 = [0]
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = [0]
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected

def test_solution4():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [0]
    input2 = [1]
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = [0,1]
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected

def test_solution5():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [0,7]
    input2 = [1,3,4,5,6]
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = [0,1,2,3,4,5,6,7]
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected

def test_solution5():
    solution = Solution()
    # Get input lists and convert to nodes
    input1 = [-5,0,3]
    input2 = [-2,-1,4,6]
    l1 = solution.list_to_nodes(input1)
    l2 = solution.list_to_nodes(input2)
    expected = [-5,-2,-1,0,3,4,6]
    # Get node output and convert back to list
    output = solution.mergeTwoLists(l1,l2)
    output = output.to_list()
    assert output==expected