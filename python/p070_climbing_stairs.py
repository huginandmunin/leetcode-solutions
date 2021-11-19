class Solution:
    def climbStairs(self, n: int) -> int:
        """ Working out the first few solutions manually shows that the
            numbers of possible ways follows a Fibonacci sequence:
            n=1, output=1
            n=2, output=2
            n=3, output=3
            n=4, output=5
            ...
        """

        if (n==1 or n==2):
            return n

        i = 2
        prev = 1
        current = 2

        while i < n:
            sum = prev + current
            prev = current
            current = sum
            i += 1

        return sum

