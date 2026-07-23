import queue


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = []
        reverse = False
        q = queue.Queue()
        q.put(root)
        
        
        while not q.empty():
            l = q.qsize()
            lvl = []
            
            
            for _ in range(l):
                n = q.get()
                
                
                if n:
                    q.put(n.left)
                    q.put(n.right)
                    lvl.append(n.val)
            
            
            if lvl:
                if reverse:
                    lvls.append(lvl[:: -1])
                else:
                    lvls.append(lvl)
            
            
            reverse = not reverse
        
        
        return lvls