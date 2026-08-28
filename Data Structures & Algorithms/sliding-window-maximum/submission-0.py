class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        L = R = 0 
        Result = []
        while R < len(nums):
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)
            if q[0] < L:
                q.popleft()
            if R - L + 1  == k:
                Result.append(nums[q[0]])
                L += 1
            R += 1
        return Result
