class Solution:
    def countHomogeneous(self, s: str) -> int:

        lengths = []
        # Count the lengths of the homogeneous substrings.
        # Would have been faster to use itertools.groupby(s)
        count = 0
        prev = s[0]
        for x in s:
            if x == prev:
                count += 1            
            else:
                lengths.append(count)
                count = 1
            prev = x
            print(f'x={x}')
        lengths.append(count)

        # For each length, n, add (n+1)*n//2. If n > root(m), then use modulo
        # of each factor, ie, ((n+1)*(n//2))%m = ((n+1)%m*(n//2)%m) %m
        result = 0
        m = 10**9 + 7
        rootm = m**0.5
        for n in lengths:
            # Handle the product as %m for n > m**0.5.
            if n<=rootm:
                result += ((n+1)*n)//2
            else:
                result += (((n+1)%m)*((n//2)%m))%m

        return result
