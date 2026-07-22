class Solution:
    def numDecodings(self, s: str) -> int:
        return 0 if s[0] == '0' else reduce(lambda a, n: (a[1], (a[0] if n[1] == '0' else a[0]+a[1]) if ('1','0') <= n <= ('2','6') else (0 if n[1] == '0' else a[1])), pairwise(s), (1, 1))[1]