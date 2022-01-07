from p017_letter_combinations_of_a_phone_number import Solution


def test_solution1():
    solution = Solution()
    input = "23"
    expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert solution.letterCombinations(input)==expected

def test_solution2():
    solution = Solution()
    input = ""
    expected = []
    assert solution.letterCombinations(input)==expected

def test_solution3():
    solution = Solution()
    input = "2"
    expected = ["a","b","c"]
    assert solution.letterCombinations(input)==expected