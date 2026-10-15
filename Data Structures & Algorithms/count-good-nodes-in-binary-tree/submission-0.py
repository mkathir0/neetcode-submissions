# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result=0
        def depth(root,maxi):
        
            if not root:
                return

            if root.val>=maxi:
                maxi=max(root.val,maxi)
                nonlocal result
                result+=1
            
            
            left=depth(root.left,maxi)
            right=depth(root.right,maxi)
        
        depth(root,root.val)
        return result