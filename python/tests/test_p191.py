from p191_number_of_1_bits import Solution

def test_solution1():
    solution = Solution()
    n = 0B00000000000000000000000000001011
    expected = 3
    assert solution.hammingWeight(n)==expected

def test_solution2():
    solution = Solution()
    n = 0B00000000000000000000000010000000
    expected = 1
    assert solution.hammingWeight(n)==expected

def test_solution3():
    solution = Solution()
    n = 0B11111111111111111111111111111101
    expected = 31
    assert solution.hammingWeight(n)==expected

def test_solution4():
    solution = Solution()
    n = 0B00000000000000000000000000000000
    expected = 0
    assert solution.hammingWeight(n)==expected