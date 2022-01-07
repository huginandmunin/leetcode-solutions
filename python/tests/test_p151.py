from p151_reverse_words_in_string import Solution

def test_solution1():
    solution = Solution()
    input = "the sky is blue"
    expected = "blue is sky the"
    assert solution.reverseWords(input)==expected

def test_solution2():
    solution = Solution()
    input = "  hello world  "
    expected = "world hello"
    assert solution.reverseWords(input)==expected

def test_solution3():
    solution = Solution()
    input = "a good   example"
    expected = "example good a"
    assert solution.reverseWords(input)==expected

def test_solution4():
    solution = Solution()
    input = "  Bob    Loves  Alice   "
    expected = "Alice Loves Bob"
    assert solution.reverseWords(input)==expected

def test_solution5():
    solution = Solution()
    input = "Alice does not even like bob"
    expected = "bob like even not does Alice"
    assert solution.reverseWords(input)==expected