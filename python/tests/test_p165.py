import sys
sys.path.append("..")

from p165_compare_version import Solution


def test_solution1():
    solution = Solution()
    version1 = "1.01"
    version2 = "1.001"
    expected = 0
    assert solution.compareVersion(version1,version2)==expected


def test_solution2():
    solution = Solution()
    version1 = "0.1"
    version2 = "1.1"
    expected = -1
    assert solution.compareVersion(version1,version2)==expected


def test_solution3():
    solution = Solution()
    version1 = "1.0"
    version2 = "1.0.0"
    expected = 0
    assert solution.compareVersion(version1,version2)==expected


def test_solution4():
    solution = Solution()
    version1 = "1.0.1"
    version2 = "1"
    expected = 1
    assert solution.compareVersion(version1,version2)==expected


def test_solution5():
    solution = Solution()
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    expected = -1
    assert solution.compareVersion(version1,version2)==expected


