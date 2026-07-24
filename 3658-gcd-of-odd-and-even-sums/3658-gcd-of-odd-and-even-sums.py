class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        total = 2 * n * n + n  # odd + even
        odd = (total - n) / 2
        even = (total + n) / 2
        while odd:  # Finding GCD
            even, odd = odd, even % odd
        return int(even)