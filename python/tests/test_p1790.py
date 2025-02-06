from p1790_check_if_one_string_swap_can_make_strings_equal import Solution


def test_solution1():
    solution = Solution()
    s1 = "bank"
    s2 = "kanb"
    expected = True
    assert solution.areAlmostEqual(s1,s2)==expected

def test_solution2():
    solution = Solution()
    s1 = "attack"
    s2 = "defend"
    expected = False
    assert solution.areAlmostEqual(s1,s2)==expected

def test_solution3():
    solution = Solution()
    s1 = "kelb"
    s2 = "kelb"
    expected = True
    assert solution.areAlmostEqual(s1,s2)==expected