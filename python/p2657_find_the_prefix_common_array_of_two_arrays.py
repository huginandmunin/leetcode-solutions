from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        count = 0
        common = []

        for i in range(len(A)):
            int_a = A[i]
            int_b = B[i]
            if int_a == int_b:
               count += 1
               common.append(count)
            else:
                if int_a in set_b:
                    count += 1
                    set_b.remove(int_a)
                else:
                    set_a.add(int_a)
                if int_b in set_a:
                    count += 1
                    set_a.remove(int_b)
                else:
                    set_b.add(int_b)
                common.append(count)

        return common       
 