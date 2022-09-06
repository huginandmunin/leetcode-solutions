class Solution:
    def secondHighest(self, s: str) -> int:
        """ 
        Create a set of all the digits. Convert the set to a list and take
        the second to last item.
        """
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))

        if len(digits)>1:
            l=list(digits)
            l.sort()
            return int(l[-2])
        else:
            return -1

