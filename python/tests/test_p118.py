from p118_pascals_triangle import Solution

def test_solution1():
    solution = Solution()
    input = 5
    expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert solution.generate(input)==expected

def test_solution2():
    solution = Solution()
    input = 1
    expected = [[1]]
    assert solution.generate(input)==expected