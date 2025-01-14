class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution():
    def isSameTree(self,p:TreeNode,q:TreeNode)->bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val!=q.val:
            return False
        else:
           return (self.isSameTree(p.left,q.left) and
            self.isSameTree(p.right,q.right))

p=TreeNode([1,2,3])
q=TreeNode([1,2,3])
s=Solution()
print(s.isSameTree(p,q))