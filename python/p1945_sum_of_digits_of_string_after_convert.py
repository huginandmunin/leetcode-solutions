class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        Convert string of letters into corresponding digits (a=1, b=2, ...)
        Do a sum of digits k times and return. Uses the algorithm from the Add Digits problem. 
        """

        ints = [str(ord(x)-ord('a')+1) for x in list(s)]
        num = int(''.join(ints))
        
        for i in range(k):
            # Sum digits starting with least significant
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            # Swap out sum and num
            num = sum

        return num
