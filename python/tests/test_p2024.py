from p2024_check_if_numbers_are_ascending_in_sequence import Solution


def test_solution1():
    solution = Solution()
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    assert solution.areNumbersAscending(s)==True

def test_solution2():
    solution = Solution()
    s = "hello world 5 x 5"
    assert solution.areNumbersAscending(s)==False

def test_solution3():
    solution = Solution()
    s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
    assert solution.areNumbersAscending(s)==False

def test_solution4():
    solution = Solution()
    s = "4 5 11 26"
    assert solution.areNumbersAscending(s)==True

def test_solution5():
    solution = Solution()
    s = "0 is more lonely that 1"
    assert solution.areNumbersAscending(s)==True
