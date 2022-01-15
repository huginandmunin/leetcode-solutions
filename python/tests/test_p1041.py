from p1041_robot_bounded_in_circle import Solution

def test_solution1():
    solution = Solution()
    instructions = "GGLLGG"
    expected = True
    assert solution.isRobotBounded(instructions)==expected

def test_solution2():
    solution = Solution()
    instructions = "GG"
    expected = False
    assert solution.isRobotBounded(instructions)==expected

def test_solution3():
    solution = Solution()
    instructions = "GL"
    expected = True
    assert solution.isRobotBounded(instructions)==expected

def test_solution4():
    solution = Solution()
    instructions = "GLGLGGLGL"
    expected = False
    assert solution.isRobotBounded(instructions)==expected
