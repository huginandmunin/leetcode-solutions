class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        """
        char_positions = {}
        result = -1

        for i, c in enumerate(s):
            if c not in char_positions.keys():
                # Set the first and last indexes the same for the first occurrence
                char_positions[c] = {'first': i, 'last': i}
            else:
                # For subsequent occurrence, set the last index and check if this is a longer substring
                char_positions[c]['last']=i
                result = max(result, char_positions[c]['last'] - char_positions[c]['first'] - 1)
        return result   
