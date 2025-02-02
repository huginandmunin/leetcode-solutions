from p1752_check_if_array_is_sorted_and_rotated import Solution


def test_solution1():
    solution = Solution()
    nums = [3,4,5,1,2]
    expected = True
    assert solution.check(nums)==expected


def test_solution2():
    solution = Solution()
    nums = [2,1,3,4]
    expected = False
    assert solution.check(nums)==expected


def test_solution3():
    solution = Solution()
    nums = [1,2,3]
    expected = True
    assert solution.check(nums)==expected