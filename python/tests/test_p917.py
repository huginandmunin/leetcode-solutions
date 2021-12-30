from p917_reverse_only_letters import Solution


def test_solution1():
    solution = Solution()
    s = "ab-cd"
    expected = "dc-ba"
    assert solution.reverseOnlyLetters(s)==expected

def test_solution2():
    solution = Solution()
    s = "a-bC-dEf-ghIj"
    expected = "j-Ih-gfE-dCba"
    assert solution.reverseOnlyLetters(s)==expected

def test_solution3():
    solution = Solution()
    s = "Test1ng-Leet=code-Q!"
    expected = "Qedo1ct-eeLg=ntse-T!"
    assert solution.reverseOnlyLetters(s)==expected

def test_solution4():
    solution = Solution()
    s = "AaW;c?["
    expected = "cWa;A?["
    assert solution.reverseOnlyLetters(s)==expected