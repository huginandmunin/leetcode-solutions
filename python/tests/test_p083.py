import sys
sys.path.append("..")

from p083_remove_duplicates_from_sorted_list import Solution, ListNode

def test_solution1():
    solution = Solution()
    l1 = solution.list_to_nodes([1,1,2])
    assert solution.deleteDuplicates(l1).to_str()=='[1,2]'

def test_solution2():
    solution = Solution()
    l2 = solution.list_to_nodes([1,1,2,3,3])
    assert solution.deleteDuplicates(l2).to_str()=='[1,2,3]'