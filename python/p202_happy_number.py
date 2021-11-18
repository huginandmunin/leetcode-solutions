class Solution:
    def isHappy(self, n: int) -> bool:
        """ Replace number by sum of squares of digits. 
            Repeat until number=1 or repeats. 
        """

        if n == 1:
            return True

        list_n = [n]
        print(f'n={n}')
        while n > 1:
            digits = list(str(n))
            n = 0
            for d in digits:
                n += int(d)*int(d)
            print(f'digits={digits}, n={n}')
            if n == 1:
                return True
            if n in list_n:
                return False
            list_n.append(n)
