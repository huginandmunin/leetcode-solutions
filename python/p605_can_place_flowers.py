from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if flowerbed == [0] and n == 1:
            return True
        
        # max possible is from [1, 0, 1, 0, 1, 0 ...]
        max = (len(flowerbed) + 1) // 2
        if n > max:
            return False
        
        window = 3
        count = 0

        # edge case
        if flowerbed[:2] == [0, 0]:
            count += 1
            flowerbed[:2] = [1, 0]
            if count == n:                
                return True
            
        j = 1
        while j <= len(flowerbed)-window:
            if flowerbed[j:j+window] == [0, 0, 0]:
                count += 1
                if count == n:
                    return True
                flowerbed[j:j+window] = [0, 1, 0]
                j += 2
            else:
                j += 1

        # edge case
        if flowerbed[-2:] == [0, 0]:
            count += 1
            if count == n:
                return True
                       
        return False

