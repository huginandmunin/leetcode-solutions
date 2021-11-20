from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ Given an array of points where 
            points[i] = [xi, yi] 
            represents a point on the X-Y plane and an integer k, 
            return the k closest points to the origin (0, 0).
        """
        if k==0 or len(points)==0 or points is None:
            return []

        # Create a list of points and the square of the distance to origin
        points_dict = [{"x": p[0],
                        "y": p[1],
                        "d2": p[0]*p[0] + p[1]*p[1]}
                        for p in points]
        # Sort the list by square of distance
        points_sorted = sorted(points_dict, key=lambda k:k['d2'])
        # Grab the first k items
        points_sorted = points_sorted[0:k]
        # Convert back to list of points
        points_closest = [[p["x"],p["y"]] for p in points_sorted]
        return points_closest


if __name__ == "__main__":
    solution = Solution()
    points = [[1,3],[-2,2]]
    k=1
    result = solution.kClosest(points,k)
    print(f'point={points}, k={k}, result={result}')

    points = [[3,3],[5,-1],[-2,4]]
    k=2
    result = solution.kClosest(points,k)
    print(f'point={points}, k={k}, result={result}')

    points = [[3,3],[5,-1],[-2,4]]
    k=0
    result = solution.kClosest(points,k)
    print(f'point={points}, k={k}, result={result}')

    points = []
    k=3
    result = solution.kClosest(points,k)
    print(f'point={points}, k={k}, result={result}')