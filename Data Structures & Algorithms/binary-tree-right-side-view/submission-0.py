# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def depth(root,level):

            if not root:
                return
            
            if level==len(res):
                res.append(root.val)
            
            right=depth(root.right,level+1)
            left=depth(root.left,level+1)

        depth(root,0)
        return res