class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        distance = []
        for i in range(n):
            x, y = points[i][0], points[i][1]
            fromOrigin = ((x ** 2) + (y ** 2)) ** 0.5
            print(fromOrigin)
            heapq.heappush(distance, [-fromOrigin, i])
            if len(distance) > k:
                heapq.heappop(distance)
    
        res = [points[i] for [_, i] in distance]
        return res

        