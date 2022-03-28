import re

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        """
        A sentence has words or numbers separated by spaces. Check that the numbers are increasing. 
        eg, "a puppy has 2 eyes 4 legs".
        
        This solution will correctly handle an input string with 0 as the first number,
        eg, "0 is more lonely than 1". 
        Some solutions initialize the previous value as 0. Those will give an incorrect False
        for the above input. 
        """
        sl = s.split()
        previous = None
        for t in sl:
            if re.match('^\\d+$',t):
                t_int = int(t)
                if previous and t_int <= previous:
                    return False
                previous = t_int

        return True
