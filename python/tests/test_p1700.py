import sys
sys.path.append("..")

from p1700_number_of_students_unable_to_eat_lunch import Solution


def test_solution1():
    solution = Solution()
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    expected=0
    assert solution.countStudents(students,sandwiches)==expected


def test_solution2():
    solution = Solution()
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    expected=3
    assert solution.countStudents(students,sandwiches)==expected


def test_solution3():
    solution = Solution()
    students = [1,1,1,1,1]
    sandwiches = [0,0,0]
    expected=5
    assert solution.countStudents(students,sandwiches)==expected


def test_solution4():
    solution = Solution()
    students = [1]
    sandwiches = [1]
    expected=0
    assert solution.countStudents(students,sandwiches)==expected