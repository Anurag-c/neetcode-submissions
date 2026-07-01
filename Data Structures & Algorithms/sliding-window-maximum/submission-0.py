class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        start, end = 0, 0

        while end < n:
            # remove expired
            while q and q[0] < start:
                q.popleft()

            # expand window
            while q and nums[end] > nums[q[-1]]:
                q.pop()
            q.append(end)
            end += 1

            # when k size window
            if end - start == k:
                res.append(nums[q[0]])
                start += 1

        return res
        