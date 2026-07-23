# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        min_depth = 0 
        current_depth = 1
        def goes_next(node):
            nonlocal min_depth
            nonlocal current_depth
            if node is None:
                return 
            if node.right is None and node.left is None: 
                if min_depth == 0:
                    min_depth = current_depth
                else:
                    min_depth = min(min_depth, current_depth)
                
            else:
                if node.right is not None:
                    current_depth += 1
                    goes_next(node.right)
                if node.left is not None:
                    current_depth += 1 
                    goes_next(node.left)
            current_depth -= 1
        goes_next(root)
        return min_depth
                
            
            
        