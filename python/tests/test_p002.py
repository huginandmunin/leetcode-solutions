from p002_add_two_numbers import Solution, ListNode

def test_solution1():
    solution = Solution()
    l1 = solution.list_to_nodes([2,4,3])
    l2 = solution.list_to_nodes([5,6,4])
    expected = '[7,0,8]'
    assert solution.addTwoNumbers(l1,l2).to_str()==expected

def test_solution2():
    solution = Solution()
    l1 = solution.list_to_nodes([0])
    l2 = solution.list_to_nodes([0])
    expected = '[0]'
    assert solution.addTwoNumbers(l1,l2).to_str()==expected

def test_solution3():
    solution = Solution()
    l1 = solution.list_to_nodes([9,9,9,9,9,9,9])
    l2 = solution.list_to_nodes([9,9,9,9])
    expected = '[8,9,9,9,0,0,0,1]'
    assert solution.addTwoNumbers(l1,l2).to_str()==expected