from p190_reverse_bits import Solution


def test_solution1():
    solution = Solution()
    n = 0B00000010100101000001111010011100
    expected = 964176192
    assert solution.reverseBits(n)==expected

def test_solution2():
    solution = Solution()
    n = 0B11111111111111111111111111111101
    expected = 3221225471
    assert solution.reverseBits(n)==expected