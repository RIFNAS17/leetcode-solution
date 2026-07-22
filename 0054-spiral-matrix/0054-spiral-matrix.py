class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        A = []

        while matrix:
            A += matrix.pop(0)
            for row in matrix:
                if row:
                    A.append(row.pop())
            if matrix:
                A += matrix.pop()[::-1]
            for row in matrix[::-1]:
                if row:
                    A.append(row.pop(0))
        return A