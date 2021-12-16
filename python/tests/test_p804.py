from p804_unique_morse_words import Solution

def test_solution1():
    solution = Solution()
    words = ["gin","zen","gig","msg"]
    expected = 2
    assert solution.uniqueMorseRepresentations(words)==expected

def test_solution2():
    solution = Solution()
    words = ["a"]
    expected = 1
    assert solution.uniqueMorseRepresentations(words)==expected