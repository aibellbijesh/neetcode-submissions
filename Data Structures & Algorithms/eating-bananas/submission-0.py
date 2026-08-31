class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            hours = 0
            m = (l + r) // 2
            for p in piles:
                hours += (p + m - 1) // m
            if hours <= h:
                result = m
                r = m - 1
            else:
                l = m + 1
        return result