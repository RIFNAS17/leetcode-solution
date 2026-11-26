class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return [i for sub in matrix for i in sub if i ==target]