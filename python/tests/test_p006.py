import sys
sys.path.append("..")

from p006_zig_zag_conversion import Solution


def test_solution1():
    solution = Solution()
    s= "PAYPALISHIRING"
    numRows = 3
    expected = "PAHNAPLSIIGYIR"
    assert solution.convert(s,numRows)==expected

def test_solution2():
    solution = Solution()
    s= "PAYPALISHIRING"
    numRows = 4
    expected = "PINALSIGYAHRPI"
    assert solution.convert(s,numRows)==expected

def test_solution3():
    solution = Solution()
    s= "A"
    numRows = 1
    expected = "A"
    assert solution.convert(s,numRows)==expected

def test_solution4():
    solution = Solution()
    s= "ABABABAB"
    numRows = 2
    expected = "AAAABBBB"
    assert solution.convert(s,numRows)==expected