class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        Step through characters. If char is digit then remove from string and compare with max. 
        """
        max = -1
        digit_str = str(digit)
        for j in range(len(number)):
            if number[j]==digit_str:
                new_number = int(number[:j] + number[j+1:])
                if new_number > max:
                    max = new_number

        return str(max)
