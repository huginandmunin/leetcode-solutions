class Solution:
    def numSub(self, s: str) -> int:
        """
        Given a binary string s, return the number of substrings 
        with all characters 1's. Since the answer may be too large, 
        return it modulo 10**9 + 7.
        """

        lengths = []
        # Count the lengths of substrings of only 1s. 
        # Could also use s.split('0') then get lengths of '1's.
        count = 0
        for x in s:
            if x == '1':
                count += 1            
            else:
                if count:
                    lengths.append(count)
                count = 0
        # Handle case of string ending in '1'
        if x == '1':
            lengths.append(count)

        # For each length, n, add (n+1)*n//2. If n > 1000000007**0.5, then use modulo
        # of each factor, ie, ((n+1)*(n//2))%m = ((n+1)%m*(n//2)%m) %m
        result = 0
        m = 1000000007
        for n in lengths:
            # Handle the product as %m for n > m**0.5.
            if n<=31621:
                result += ((n+1)*n)//2
            else:
                result += (((n+1)%m)*((n//2)%m))%m

        return result

