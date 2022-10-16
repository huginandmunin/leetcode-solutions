class Solution:
    def myAtoi(self, s: str) -> int:

        # default sign and integer value
        sign = '+'
        i = 0

        # Convert string to list
        l = [c for c in s]
        if len(l)==0:
            return i

        # pop off leading whitespaces
        while (len(l) and l[0]==' '):
            l.pop(0)

        if len(l)==0:
            return i

        # look for a plus or minus sign
        if l[0] in ['-', '+']:
            sign = l[0]
            l.pop(0)

        # accumulate digits, convert to integer value
        digits = ['0','1','2','3','4','5','6','7','8','9']
        for d in l:
            if d in digits:
                i = i*10 + ord(d)-ord('0')
            else:
                break

        # change sign if necessary       
        if sign == '-':
            i = i * -1

        # check limit of integer
        max = 2 ** 31 - 1
        min = -1 * (max + 1)
        if i > max:
            i = max
        elif i < min:
            i = min

        return i