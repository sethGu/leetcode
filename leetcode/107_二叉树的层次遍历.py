# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root: return res
        def helper(node,lvl):
            if len(res)==lvl: res.append([])
            res[lvl].append(node.val)
            if node.left: helper(node.left,lvl+1)
            if node.right: helper(node.right,lvl+1)
        helper(root,0)
        tmp,i=[],0
        while res:
            tmp.append(res.pop())
        return tmp