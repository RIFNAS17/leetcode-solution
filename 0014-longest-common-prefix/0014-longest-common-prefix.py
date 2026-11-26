class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return strs[0][:max([i for i in range(200) if all(i <= len(s) and s[:i] == strs[0][:i] for s in strs)] + [0])]