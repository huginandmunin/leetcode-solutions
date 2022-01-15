from p657_robot_return_to_origin import Solution

def test_solution1():
    solution = Solution()
    moves = "UD"
    expected = True
    assert solution.judgeCircle(moves)==expected

def test_solution2():
    solution = Solution()
    moves = "LL"
    expected = False
    assert solution.judgeCircle(moves)==expected

def test_solution3():
    solution = Solution()
    moves = "LURDLURD"
    expected = True
    assert solution.judgeCircle(moves)==expected

def test_solution4():
    solution = Solution()
    moves = ""
    expected = True
    assert solution.judgeCircle(moves)==expected
