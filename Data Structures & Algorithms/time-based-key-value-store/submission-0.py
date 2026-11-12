class TimeMap:

    def __init__(self):
        self.store = {} # key -> [(value, ts)]
    
    def _binarySearch(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        low, high = 0, len(values) - 1
        res = ""

        while low <= high:
            mid = (low + high) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        
        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        return self._binarySearch(key, timestamp)
        


        
