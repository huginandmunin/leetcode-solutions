import sys
sys.path.append("..")

from p273_integer_to_english_words import Solution

def test_solution1():
    solution = Solution()
    input = 0
    expected = 'Zero'
    assert solution.numberToWords(input)==expected

def test_solution2():
    solution = Solution()
    input = 4
    expected = 'Four'
    assert solution.numberToWords(input)==expected

def test_solution3():
    solution = Solution()
    input = 10
    expected = 'Ten'
    assert solution.numberToWords(input)==expected

def test_solution4():
    solution = Solution()
    input = 12
    expected = 'Twelve'
    assert solution.numberToWords(input)==expected

def test_solution5():
    solution = Solution()
    input = 45
    expected = 'Forty Five'
    assert solution.numberToWords(input)==expected

def test_solution6():
    solution = Solution()
    input =99
    expected = 'Ninety Nine'
    assert solution.numberToWords(input)==expected

def test_solution7():
    solution = Solution()
    input = 100
    expected = 'One Hundred'
    assert solution.numberToWords(input)==expected

def test_solution8():
    solution = Solution()
    input = 101
    expected = 'One Hundred One'
    assert solution.numberToWords(input)==expected

def test_solution9():
    solution = Solution()
    input = 123
    expected = 'One Hundred Twenty Three'
    assert solution.numberToWords(input)==expected

def test_solution10():
    solution = Solution()
    input = 1023
    expected = 'One Thousand Twenty Three'
    assert solution.numberToWords(input)==expected

def test_solution11():
    solution = Solution()
    input = 12345
    expected = 'Twelve Thousand Three Hundred Forty Five'
    assert solution.numberToWords(input)==expected

def test_solution12():
    solution = Solution()
    input = 12045
    expected = 'Twelve Thousand Forty Five'
    assert solution.numberToWords(input)==expected

def test_solution13():
    solution = Solution()
    input = 50868
    expected = 'Fifty Thousand Eight Hundred Sixty Eight'
    assert solution.numberToWords(input)==expected

def test_solution14():
    solution = Solution()
    input = 100011
    expected = 'One Hundred Thousand Eleven'
    assert solution.numberToWords(input)==expected

def test_solution15():
    solution = Solution()
    input = 1234567
    expected = 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'
    assert solution.numberToWords(input)==expected

def test_solution16():
    solution = Solution()
    input = 1034567
    expected = 'One Million Thirty Four Thousand Five Hundred Sixty Seven'
    assert solution.numberToWords(input)==expected

def test_solution17():
    solution = Solution()
    input = 1234567891
    expected = 'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One'
    assert solution.numberToWords(input)==expected

def test_solution18():
    solution = Solution()
    input = 9999999999
    expected = 'Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine'
    assert solution.numberToWords(input)==expected