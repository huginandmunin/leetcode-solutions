from p1523_count_odd_numbers_in_an_interval_range import Solution


def test_solution1():
    solution = Solution()
    low = 3
    high = 7
    expected = 3
    assert solution.countOdds(low,high)==expected

def test_solution2():
    solution = Solution()
    low = 8
    high = 10
    expected = 1
    assert solution.countOdds(low,high)==expected

def test_solution3():
    solution = Solution()
    low = 0
    high = 1
    expected = 1
    assert solution.countOdds(low,high)==expected

def test_solution4():
    solution = Solution()
    low = 0
    high = 2
    expected = 1
    assert solution.countOdds(low,high)==expected