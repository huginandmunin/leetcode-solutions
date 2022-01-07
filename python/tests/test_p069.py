from p069_sqrt import Solution


def test_solution1():
    solution = Solution()
    input = 4
    expected = 2
    assert solution.mySqrt(input)==expected

def test_solution2():
    solution = Solution()
    input = 6
    expected = 2
    assert solution.mySqrt(input)==expected

def test_solution3():
    solution = Solution()
    input = 9
    expected = 3
    assert solution.mySqrt(input)==expected

def test_solution4():
    solution = Solution()
    input = 10
    expected = 3
    assert solution.mySqrt(input)==expected

def test_solution5():
    solution = Solution()
    input = 1
    expected = 1
    assert solution.mySqrt(input)==expected
