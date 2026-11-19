class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-w for w in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            rem = abs(x - y)
            if rem > 0:
                heapq.heappush(stones, -rem)
        
        if len(stones) == 0:
            return 0
        
        return heapq.heappop(stones) * -1

        