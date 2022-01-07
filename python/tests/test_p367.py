from p367_valid_perfect_square import Solution


def test_solution1():
    solution = Solution()
    assert solution.isPerfectSquare(4)==True

def test_solution1():
    solution = Solution()
    assert solution.isPerfectSquare(5)==False

def test_solution2():
    solution = Solution()
    assert solution.isPerfectSquare(100)==True

def test_solution3():
    solution = Solution()
    assert solution.isPerfectSquare(101)==False