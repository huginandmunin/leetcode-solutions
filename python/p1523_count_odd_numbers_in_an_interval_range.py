class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Given two non-negative integers low and high. 
        Return the count of odd numbers between low and high (inclusive).

        Hint: check if interval (high-low+1) is even/odd and
        check if low is even/odd (high will be the same when interval is odd)
        """
        
        # Zero is neither even or odd
        if low == 0 and high == 0:
            return 0
        if low == 0 and high >= 1:
            low = 1

        interval = high - low + 1
        # Default number of odds is half of the interval
        n_odd = interval // 2
        # Add 1 for odd intervals that start with an odd number
        if (interval%2==1) and (low%2==1):
            n_odd += 1

        return n_odd