from p070_climbing_stairs import Solution


def test_solution1():
    solution = Solution()
    input = 1
    expected = 1
    assert solution.climbStairs(input)==expected

def test_solution2():
    solution = Solution()
    input = 2
    expected = 2
    assert solution.climbStairs(input)==expected

def test_solution3():
    solution = Solution()
    input = 3
    expected = 3
    assert solution.climbStairs(input)==expected

def test_solution4():
    solution = Solution()
    input = 5
    expected = 8
    assert solution.climbStairs(input)==expected

def test_solution5():
    solution = Solution()
    input = 10
    expected = 89
    assert solution.climbStairs(input)==expected