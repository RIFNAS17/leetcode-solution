class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        return (f:=cache(lambda i,j:i<len(t) and t[i][j]+min(f(i+1,j),f(i+1,j+1))))(0,0)