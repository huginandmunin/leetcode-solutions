from p011_container_with_most_water import Solution


def test_solution1():
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
    assert solution.maxArea(height)==expected


def test_solution2():
    solution = Solution()
    height = [1,1]
    expected = 1
    assert solution.maxArea(height)==expected


def test_solution3():
    solution = Solution()
    height = [4,3,2,1,4]
    expected = 16
    assert solution.maxArea(height)==expected


def test_solution3():
    solution = Solution()
    height = [1,2,1]
    expected = 2
    assert solution.maxArea(height)==expected
