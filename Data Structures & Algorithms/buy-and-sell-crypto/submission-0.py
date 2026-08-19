class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_p = prices[0]
        max_p = 0
        for p in prices:
            lowest_p = min(lowest_p, p)
            profit = p - lowest_p
            max_p = max(max_p, profit)
        return max_p