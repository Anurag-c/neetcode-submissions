class Solution:
    def getHoursRequired(self, piles: List[int], h: int, bananaPerHour: int) -> int:
        reqHours = 0
        for bananas in piles:
            reqHours = reqHours + math.ceil(float(bananas) / bananaPerHour)
        return reqHours


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        speed = high
        while low <= high:
            mid = (low + high) // 2
            reqHours = self.getHoursRequired(piles, h, mid)
            if reqHours <= h:
                speed = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return speed


        
        