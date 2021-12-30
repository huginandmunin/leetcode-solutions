class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Given a string s, reverse the string according to the following rules:

        All the characters that are not English letters remain in the same position.
        All the English letters (lowercase or uppercase) should be reversed.

        Return s after reversing it.

        Solution compares ordinal number against list of ascii codes. 
        Might go faster with s[i].isalpha, s[i].isnumeric.
        """

        # Set beginning and end indexes of string, convert string to list
        i = 0
        j = len(s)-1
        sl = list(s)
        
        # Swap if values are alphanumeric
        while i < j:
            while i<j and not sl[i].isalpha():
                i += 1
            while j>i and not sl[j].isalpha():
                j -= 1
            sl[i],sl[j] = sl[j],sl[i]
            i += 1
            j -= 1

        # Return string
        return ''.join(sl) 

if __name__ == "__main__":
    solution = Solution()
    s = 'ab-cd'
    result = solution.reverseOnlyLetters(s)