from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        Can form a prefix array of non-increasing days
        and a suffix array of non-decreasing days
        """

        array_len = len(security)
        good_days = []
        prefix = [0]
        suffix = [0]* array_len
        num_non_increasing = 0
        num_non_decreasing = 0
        for i in range(1,array_len):
            if security[i] <= security[i - 1]:
                num_non_increasing += 1
            else:
                num_non_increasing = 0
            prefix.append(num_non_increasing)
        print(f"Prefix {prefix}")


        for i in range(array_len-2,-1,-1):
            if security[i] <= security[i+1]:
                num_non_decreasing += 1
            else:
                num_non_decreasing = 0
            suffix[i] = num_non_decreasing

        print(f"Suffix = {suffix}")

        # find the days with prefix > time and suffix > time
        for i in range(array_len):
            print(f"Working on i={i}, prefix = {prefix[i]}, suffix={suffix[i]}")
            if prefix[i] >= time and suffix[i] >= time:
                good_days.append(i)

        return good_days


                 

                          
            
            

        return good_days