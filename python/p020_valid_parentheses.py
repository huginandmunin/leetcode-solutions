class Solution:

    def isValid(self, s: str) -> bool:
        """ This method utilizes a stack for storing the
            parentheses. 
            
            The method iterates over the parentheses characters.
            Opening parentheses are pushed into 
            the stack. When a closing parenthesis is found it
            is compared against the most recent opening parethesis.
        """

        # Initialize
        oc_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        openers = oc_dict.keys()
        closers = oc_dict.values()
        oc_stack = []

        # Strings of paren-only must have an even number of characters > 0
        if (len(s) == 0 or len(s) % 2 == 1):
            return False

        for char in s:
            if char in openers:
                oc_stack.append(char)
            elif char in closers:
                # Check for match in non-empty stack    
                if (len(oc_stack) == 0 or char != oc_dict[oc_stack.pop()]):
                    return False
            else:
                # Not a parenthesis
                return False

        # Check that all openers have been matched and pulled out       
        if len(oc_stack)==0:
            return True
        else:
            return False

