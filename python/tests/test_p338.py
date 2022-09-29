from p338_counting_bits import Solution


def test_solution1():
    solution = Solution()
    n = 2
    expected = [0,1,1]
    assert solution.countBits(n)==expected

def test_solution2():
    solution = Solution()
    n = 5
    expected = [0,1,1,2,1,2]
    assert solution.countBits(n)==expected

