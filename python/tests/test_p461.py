from p461_hamming_distance import Solution


def test_solution1():
    solution = Solution()
    x=1
    y=4
    expected = 2
    assert solution.hammingDistance(x,y)==expected


def test_solution2():
    solution = Solution()
    x=3
    y=1
    expected = 1
    assert solution.hammingDistance(x,y)==expected


def test_solution3():
    solution = Solution()
    x=0
    y=0
    expected = 0
    assert solution.hammingDistance(x,y)==expected