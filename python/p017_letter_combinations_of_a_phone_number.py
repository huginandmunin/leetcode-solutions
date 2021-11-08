from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ For each digit, loop over corresponding letters 
            and append the letter to the items in the output list.
        """

        if not digits:
            return []

        # Initialize
        results = ['']
        letters_dict = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": []           
        }

        # Loop over digits
        dig_list = list(digits)
        while dig_list:
            new_results = []
            c = dig_list.pop(0)
            for item in results:
                for letter in letters_dict[c]:
                    # A new item in the new list is 'item + letter'
                    new_results.append(item + letter)
            results = new_results

        return results
