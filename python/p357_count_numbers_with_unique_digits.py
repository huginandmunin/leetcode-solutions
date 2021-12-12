class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Given an integer n, return the count of all numbers with 
        unique digits, x, where 0 <= x < 10n.

        Hint:
        f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) 
        [The first factor is 9 because a number cannot start with 0].
        n=0, expected=1
        n=1, expected=10
        n=2, expected=91
        n=3, expected=739
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n > 1:
            result = 10
            for k in range(2,n+1):
                result += self.count_for_k(k)
            return result


    def count_for_k(self,k):
        """
        f(k) = 9 * 9 * 8 * ... (9 - k + 2)
        """
        p = 9
        min = 9 - k + 2
        for i in range(9,min-1,-1):
            p *= i                
        return p               
            
            
 