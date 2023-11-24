from p2103_rings_and_rods import Solution


def test_solution1():
    solution = Solution()
    rings = "B0B6G0R6R0R6G9"
    expected = 1
    assert solution.countPoints(rings)==expected

def test_solution2():
    solution = Solution()
    rings = "B0B6G0R6R0R6G9"
    expected = 1
    assert solution.countPoints(rings)==expected

def test_solution3():
    solution = Solution()
    rings = "G4"
    expected = 0
    assert solution.countPoints(rings)==expected