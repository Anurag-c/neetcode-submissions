import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for x in nums:
            freqMap[x] += 1

        minPq = []
        for (key, val) in freqMap.items():
            heapq.heappush(minPq, (val, key))
            if(len(minPq) > k):
                heapq.heappop(minPq)

        res = []
        for (val, key) in minPq:
            res.append(key)
        
        return res
        