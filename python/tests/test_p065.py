from p065_valid_number import Solution

# Valid numbers - integers


def test_solution1():
    solution = Solution()
    s = "0"
    assert solution.isNumber(s)==True

def test_solution2():
    solution = Solution()
    s = "2"
    assert solution.isNumber(s)==True


def test_solution3():
    solution = Solution()
    s = "0089"
    assert solution.isNumber(s)==True

# Valid numbers - decimal

def test_solution4():
    solution = Solution()
    s = "-0.1"
    assert solution.isNumber(s)==True


def test_solution5():
    solution = Solution()
    s = "+3.14"
    assert solution.isNumber(s)==True


def test_solution6():
    solution = Solution()
    s = "4."
    assert solution.isNumber(s)==True


def test_solution7():
    solution = Solution()
    s = "-.9"
    assert solution.isNumber(s)==True


# Valid numbers - scientific notation

def test_solution8():
    solution = Solution()
    s = "2e10"
    assert solution.isNumber(s)==True


def test_solution9():
    solution = Solution()
    s = "-90E3"
    assert solution.isNumber(s)==True


def test_solution10():
    solution = Solution()
    s = "3e+7"
    assert solution.isNumber(s)==True


def test_solution11():
    solution = Solution()
    s = "+6e-1"
    assert solution.isNumber(s)==True


def test_solution12():
    solution = Solution()
    s = "53.5e93"
    assert solution.isNumber(s)==True


def test_solution13():
    solution = Solution()
    s = "-123.456e789"
    assert solution.isNumber(s)==True

# Non-valid numbers

def test_solution14():
    solution = Solution()
    s = "."
    assert solution.isNumber(s)==False


def test_solution15():
    solution = Solution()
    s = "e"
    assert solution.isNumber(s)==False


def test_solution16():
    solution = Solution()
    s = "abc"
    assert solution.isNumber(s)==False


def test_solution17():
    solution = Solution()
    s = "1a"
    assert solution.isNumber(s)==False


def test_solution18():
    solution = Solution()
    s = "1e"
    assert solution.isNumber(s)==False


def test_solution19():
    solution = Solution()
    s = "e3"
    assert solution.isNumber(s)==False


def test_solution20():
    solution = Solution()
    s = "99e2.5"
    assert solution.isNumber(s)==False


def test_solution21():
    solution = Solution()
    s = "--6"
    assert solution.isNumber(s)==False


def test_solution22():
    solution = Solution()
    s = "+-3"
    assert solution.isNumber(s)==False


def test_solution23():
    solution = Solution()
    s = "+95e54e53"
    assert solution.isNumber(s)==False