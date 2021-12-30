from p2075_decode_the_slanted_ciphertext import Solution


def test_solution1():
    solution = Solution()
    encodedText = "ch   ie   pr"
    rows = 3
    expected = "cipher"
    assert solution.decodeCiphertext(encodedText,rows)==expected


def test_solution2():
    solution = Solution()
    encodedText = "iveo    eed   l te   olc"
    rows = 4
    expected = "i love leetcode"
    assert solution.decodeCiphertext(encodedText,rows)==expected


def test_solution3():
    solution = Solution()
    encodedText = "coding"
    rows = 1
    expected = "coding"
    assert solution.decodeCiphertext(encodedText,rows)==expected