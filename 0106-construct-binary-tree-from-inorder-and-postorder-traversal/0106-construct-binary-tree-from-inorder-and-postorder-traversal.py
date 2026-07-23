class Solution:
    def buildTree(self, i: List[int], p: List[int]) -> Optional[TreeNode]:
        return (f:=lambda i,p:i and TreeNode(p[-1],f(i[:(k:=i.index(p[-1]))],p[:k]),f(i[k+1:],p[k:-1])) or None)(i,p)