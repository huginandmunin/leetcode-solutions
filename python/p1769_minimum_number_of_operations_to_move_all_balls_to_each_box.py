from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        if len(boxes) == 1:
            return [0]
        
        boxes_list = []
        for c in boxes:
            boxes_list.append(int(c))
        print(f"Boxes list = {boxes_list}")
        n_boxes = len(boxes_list)
        result = []

        # prefix sum
        # make two passes: first to count ones, second to count distance
        ps = []
        c_sum = 0
        for c in boxes_list:
            # if c_sum:
            #     c_sum += 1
            c_sum += c
            ps.append(c_sum)
        print(f"ps_sum = {ps}")
        for i in range(1,len(ps)):
            ps[i] = ps[i-1] + ps[i]
        print(f"ps_sum = {ps}")

        # suffix sum
        ss = [0] * len(boxes)
        c_sum = 0
        for i in range(len(boxes_list)-1, -1, -1):
            # if c_sum:
            #     c_sum += 1
            c_sum += boxes_list[i]
            ss[i] = c_sum
        print(f"ssum = {ss}")
        for i in range(len(boxes_list)-2, -1, -1):
            # if c_sum:
            #     c_sum += 1
            ss[i] = ss[i+1] + ss[i]
        print(f"ssum = {ss}")

        # first element is suffix[i+1] where i = 0
        result = [ss[1]]
        for i in range(1,len(boxes)-1):
            print(f"i={i}, left = {ps[i-1]}, right = {ss[i+1]}")
            result.append(ps[i-1] + ss[i+1])
        # last element is prefix[i-1] where i = len(boxes)-1
        result.append(ps[len(boxes)-2])
        return result


        

        # # This runs slow.
        # # Instead try a prefix sum and a postfix sum.
        # # sum from left (prefix) and right (postfix)
        # # ops[i] = prefix[i-1]) + postfix[i+1],
        # # where prefix[-1] = 0 and postfix[n+1]=0
        # for i in range(n_boxes):
        #     ops = 0
        #     for j in range(n_boxes):
        #         ops += (abs(j-i) * boxes_list[j])
        #         print(f"i={i}, j={j}, ops = {ops}")
        #     result.append(ops)
        # print(f"result = {result}")

        return result
                
