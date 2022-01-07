from p136_single_number import Solution

def test_solution1():
    solution = Solution()
    input = [2,2,1]
    expected = 1
    assert solution.singleNumber(input)==expected

def test_solution2():
    solution = Solution()
    input = [4,1,2,1,2]
    expected = 4
    assert solution.singleNumber(input)==expected

def test_solution3():
    solution = Solution()
    input = [1]
    expected = 1
    assert solution.singleNumber(input)==expected