class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        The method iterates over characters in the input. 
        Addition or subtraction of adjacent characters 
        is determined by comparing each input character with 
        the following character.
        """

        # Roman-Decimal dictionary
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Initialize with first character
        decimal = 0
        chars = list(s)
        char = chars.pop(0)
        if char not in roman_dict.keys():
            print(f"Invalid input: {s}")
            return None
        new_val = roman_dict[char]
        prev_val = new_val

        # Iterate over remaining characters
        for char in chars:
            if char not in roman_dict.keys():
                print(f"Invalid input: {s}")
                return None
            new_val = roman_dict[char]
            # Subtract if new_val > prev_val, else add
            if new_val > prev_val:
                # if [prev_val,new_val] not in special_combos:
                if not (prev_val in [1,10,100] and (new_val/prev_val==5 or new_val/prev_val==10)):
                    print(f"Invalid input: {s}")
                    return None
                else:                  
                    decimal -= prev_val
            else:
                decimal += prev_val
            prev_val = new_val

        decimal += new_val
        return decimal
