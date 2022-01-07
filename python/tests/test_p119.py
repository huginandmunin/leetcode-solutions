from p119_pascals_triangle_ii import Solution

def test_solution1():
    solution = Solution()
    input = 3
    expected = [1,3,3,1]
    assert solution.getRow(input)==expected

def test_solution2():
    solution = Solution()
    input = 0
    expected = [1]
    assert solution.getRow(input)==expected

def test_solution3():
    solution = Solution()
    input = 1
    expected = [1,1]
    assert solution.getRow(input)==expected