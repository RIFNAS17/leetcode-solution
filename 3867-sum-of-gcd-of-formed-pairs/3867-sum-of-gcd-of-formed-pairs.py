acc = accumulate
class Solution:
    def gcdSum(self, A):
        return (lambda pg: sum(gcd(pg[i], pg[len(A) - i - 1]) for i in range(len(A)//2)))(sorted([gcd(a, b) for a, b in zip(A, list(acc(A, max)))]))