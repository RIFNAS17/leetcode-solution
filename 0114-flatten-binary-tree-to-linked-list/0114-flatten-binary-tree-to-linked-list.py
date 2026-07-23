# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        def preorder(queue, root):
            if not root:
                return None
            
            queue.append(root)
            preorder(queue, root.left)
            preorder(queue, root.right)
            
            return queue
        
        queue = collections.deque(preorder([], root))
        
        
        while queue:
            curr=queue.popleft()
            curr.left=None
            if len(queue)>0:
                curr.right=queue[0]

        

            
        
        