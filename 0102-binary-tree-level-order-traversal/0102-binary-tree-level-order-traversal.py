# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, level, result):
        if node is None:
            return
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        self.dfs(node.left, level + 1, result)
        self.dfs(node.right, level + 1, result)
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        self.dfs(root, 0, result)
        return result