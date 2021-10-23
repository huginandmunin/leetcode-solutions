class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Let's store the substring in a list """
        list = []
        l = 0
        sub_str = ''

        # Handle edge case of empty input
        if not s:
            return 0

        for c in s:
            print(f'c={c}, l = {l}, list={list}')
            if c in list:
                # Reset if we have a new substring (if we have found a repeated character)
                if len(list) > l:
                    sub_str = ''.join(list)
                    l = len(list)
                # Split list to keep items after repeated value
                while list:
                    if list.pop(0) == c:
                        break

            # Keep adding chars for this substring
            # including the repeated char because it has been removed from head of list
            list.append(c)
        # Handle case of longest substring at end of string
        if len(list) > l:
            sub_str = ''.join(list)
            l = len(list)
        print(f'sub = {sub_str}')
        return l
