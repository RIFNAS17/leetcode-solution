class Solution:
    def canJump(self, nums: List[int]) -> bool:

        Jump= 0
        for i, num in enumerate(nums):
            if i > Jump:
                return False
            Jump = max(Jump, i + num)
        return True
