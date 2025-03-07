from p2523_closest_prime_numbers_in_range import Solution

def test_solution1():
    solution = Solution()
    left = 10
    right = 19
    expected = [11,13]
    assert solution.closestPrimes(left,right)==expected

def test_solution2():
    solution = Solution()
    left = 4
    right = 6
    expected = [-1,-1]
    assert solution.closestPrimes(left,right)==expected

def test_solution3():
    solution = Solution()
    left = 19
    right = 31
    expected = [29,31]
    assert solution.closestPrimes(left,right)==expected


def test_solution4():
    solution = Solution()
    left = 18
    right = 72
    expected = [29,31]
    assert solution.closestPrimes(left,right)==expected

def test_solution5():
    solution = Solution()
    left = 1
    right = 1000
    expected = [2,3]
    assert solution.closestPrimes(left,right)==expected