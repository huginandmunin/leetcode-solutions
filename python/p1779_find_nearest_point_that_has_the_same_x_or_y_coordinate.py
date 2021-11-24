from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """ 
        You are given two integers, x and y, which represent your current location 
        on a Cartesian grid: (x, y). You are also given an array points where 
        each points[i] = [ai, bi] represents that a point exists at (ai, bi). 
        A point is valid if it shares the same x-coordinate or the same y-coordinate 
        as your location.

        Return the index (0-indexed) of the valid point with the 
        smallest Manhattan distance from your current location. 
        If there are multiple, return the valid point with the smallest index. 
        If there are no valid points, return -1.
        """

        # Get list of points with same x or y
        dist_dict = [{'i':i,'md':abs(x-p[0])+abs(y-p[1])} 
                    for i,p in enumerate(points,0)
                    if (x==p[0] or y==p[1])]
        if len(dist_dict) < 1:
            return -1

        # Sort by Manhattan distance
        dist_sorted = sorted(dist_dict, key=lambda k:k['md'])
        # Return the index value captured in the first item in sorted dict
        return dist_sorted[0]['i']
