class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        cycle = 2 * (numRows - 1)

        for i in range(numRows):
            for j in range(i, len(s), cycle):
                ans += s[j]

                k = j + cycle - 2 * i

                if i > 0 and i < numRows - 1 and k < len(s):
                    ans += s[k]

        return ans


obj = Solution()
print(obj.convert("PAYPALISHIRING", 3))