from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        This solution implements a temporary storage. A better
        approach would be to use two pointers:
        s[i],s[end-i]=s[end-i],s[i]
        """

        # Find end and midpoint of list
        end = len(s)
        end -= 1
        mid = len(s)
        mid //= 2

        for i in range(mid):
            print(f'i={i}, end={end}')
            tmp = s[i]
            s[i] = s[end-i]
            s[end-i] = tmp

        # Adding a return statement for unit tests
        return s

        