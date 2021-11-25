from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Pass through list until person at tickets[k] has bought all of their ticket.
        At each pass decrement the number of tickets and increment the time_to_buy.
        """
        time_to_buy = 0
        n_people = len(tickets)
        while tickets[k] != 0:
            for i in range(n_people):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time_to_buy += 1
                # Stop decrementing when tickets[k]==0
                if tickets[k] == 0:
                    break
        return time_to_buy