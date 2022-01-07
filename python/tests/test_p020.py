from p020_valid_parentheses import Solution


def test_solution1():
    solution = Solution()
    input = "(("
    expected = False
    assert solution.isValid(input)==expected

def test_solution2():
    solution = Solution()
    input = "))"
    expected = False
    assert solution.isValid(input)==expected

def test_solution3():
    solution = Solution()
    input = "()"
    expected = True
    assert solution.isValid(input)==expected

def test_solution4():
    solution = Solution()
    input = "()[]{}"
    expected = True
    assert solution.isValid(input)==expected

def test_solution5():
    solution = Solution()
    input = "(]"
    expected = False
    assert solution.isValid(input)==expected

def test_solution6():
    solution = Solution()
    input = "([)]"
    expected = False
    assert solution.isValid(input)==expected

def test_solution7():
    solution = Solution()
    input = "{[]}"
    expected = True
    assert solution.isValid(input)==expected