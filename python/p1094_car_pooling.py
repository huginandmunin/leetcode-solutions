from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Hint: Sort the pickup and dropoff events by location, then process them in order."""
        # want to build a running sum of num_passengers at every stop.
        # 0 <= from_i < to_i <= 1000
             
        passengers = [0] * 1001

        for trip in trips:
            print(f"trip = {trip}")
            for i in range(trip[1], trip[2]):
                print(f"i={i}")
                passengers[i] += trip[0]
                print(f"i={i}, passengers={passengers[i]}")
                if passengers[i] > capacity:
                    return False

            print(f"Stops {passengers[0:10]}")
        return True
