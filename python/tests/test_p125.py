from p125_valid_palindrome import Solution


def test_solution1():
    solution = Solution()
    input = 'A man, a plan, a canal: Panama'
    expected = True
    assert solution.isPalindrome(input)==expected


def test_solution2():
    solution = Solution()
    input = 'race a car'
    expected = False
    assert solution.isPalindrome(input)==expected


def test_solution3():
    solution = Solution()
    input = ' '
    expected = True
    assert solution.isPalindrome(input)==expected


def test_solution4():
    solution = Solution()
    input = ' Yo! Banana Boy!'
    expected = True
    assert solution.isPalindrome(input)==expected


def test_solution5():
    solution = Solution()
    input = 'Taco  C A t'
    expected = True
    assert solution.isPalindrome(input)==expected


def test_solution6():
    solution = Solution()
    input = 'Abracadabra'
    expected = False
    assert solution.isPalindrome(input)==expected


def test_solution7():
    solution = Solution()
    input = '10-100-1000-10-100-10001-001-01-0001-001-01'
    expected = True
    assert solution.isPalindrome(input)==expected


def test_solution7():
    solution = Solution()
    input = 'asdf-asdf-asdf-asdf-asdf'
    expected = False
    assert solution.isPalindrome(input)==expected