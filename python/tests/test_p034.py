from p034_find_first_and_last import Solution


def test_solution1():
    solution = Solution()
    input = [5,7,7,8,8,10]
    target = 8
    expected = [3,4]
    assert solution.searchRange(input,target)==expected

def test_solution2():
    solution = Solution()
    input = [5,7,7,8,8,10]
    target = 6
    expected = [-1,-1]
    assert solution.searchRange(input,target)==expected

def test_solution1():
    solution = Solution()
    input = []
    target = 0
    expected = [-1,-1]
    assert solution.searchRange(input,target)==expected

def test_solution1():
    solution = Solution()
    input = [1]
    target = 1
    expected = [0,0]
    assert solution.searchRange(input,target)==expected