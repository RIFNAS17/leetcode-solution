class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        m = min(p for _, p in items)
        lim = 2 * m
        cnt = [0] * (n + 1)
        for f, p in items:
            cnt[f] += 1
        mult = [0] * (n + 1)
        for x in range(1, n + 1):
            if cnt[x]:
                mult[x] = sum(cnt[x::x]) - 1
        keys = sorted(
            p * 100000 + mult[f]
            for f, p in items
            if p < lim and mult[f]
        )
        spent = 0
        k = 0
        for key in keys:
            p = key // 100000
            d = key % 100000
            t = (budget - spent) // p
            if t > d:
                t = d
            spent += t * p
            k += t
            if t < d:
                break
        return 2 * k + (budget - spent) // m