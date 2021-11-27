from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        The sandwiches don't move so that list has to stay in order.
        The students are always churning so order doesn't matter. 
        This solution loops over the sandwiches list and looks for a matching student.
        """
        for san in sandwiches:
            if san in students:
                students.remove(san)
            else:
                break
        return len(students)

