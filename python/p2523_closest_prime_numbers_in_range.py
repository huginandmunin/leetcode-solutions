from typing import List

class Solution:
    def closestPrimes(self, left:int, right:int) -> List[int]:

        result = [-1, -1]
        primes = self.get_primes(left, right)

        if len(primes) >= 2:
            diff = primes[1] - primes[0]
            min_diff = diff
            result = [primes[0], primes[1]]
            for i in range(2,len(primes)):
                diff = primes[i] - primes[i-1]
                if diff < min_diff:
                    result = [primes[i-1], primes[i]]
                    min_diff = diff

        return result


    def get_primes(self, left: int, right: int) -> List[int]:
        """
        Use the sieve of erastothenes to generate a list of prime numbers from
        left to right
        """
        primes = [True for i in range(right+1)]
        i = 2
        while (i * i <= right):
            # if this is a prime then mark all mulitples as not prime
            if primes[i]:
                for j in range(i * i, right+1, i):
                    primes[j] = False
            i += 1

        result = []

        if left == 1:
            left = 2
        for i in range(left, right+1):
            if primes[i]:
                result.append(i)

        return result
