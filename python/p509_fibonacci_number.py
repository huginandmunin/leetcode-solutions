class Solution:
    def fib(self, n: int) -> int:
        """ Fibonacci sequence:
            F(0) = 0
            F(1) = 1
            F(2) = 1
            F(3) = 2
            F(4) = 3
            F(5) = 5
            ...
            F(n) = F(n-1) + F(n-2)
        """

        if (n==0 or n==1):
            return n

        i = 1
        prev = 0
        current = 1

        while i < n:
            sum = prev + current
            prev = current
            current = sum
            i += 1

        return sum