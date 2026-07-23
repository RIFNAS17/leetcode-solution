class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_A=float('inf')
        max_B=0
        for current in prices:
            min_A=min(current,min_A)
            max_B=max(max_B,current-min_A)
        return max_B