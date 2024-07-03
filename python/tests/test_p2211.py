from p2211_count_collisions_on_a_road import Solution

def test_solution1():
    solution = Solution()
    input = "RLR"
    expected = 2
    assert solution.countCollisions(input) == expected

def test_solution2():
    solution = Solution()
    input = "LLLSLLL"
    expected = 3
    assert solution.countCollisions(input) == expected

def test_solution3():
    solution = Solution()
    input = "LLLRLLL"
    expected = 4
    assert solution.countCollisions(input) == expected

def test_solution4():
    solution = Solution()
    input = "RRRSRRR"
    expected = 3
    assert solution.countCollisions(input) == expected

def test_solution5():
    solution = Solution()
    input = "RRRLRRR"
    expected = 4
    assert solution.countCollisions(input) == expected

def test_solution5():
    solution = Solution()
    input = "RLRSLL"
    expected = 5
    assert solution.countCollisions(input) == expected


def test_solution5():
    solution = Solution()
    input = "LLRR"
    expected = 0
    assert solution.countCollisions(input) == expected