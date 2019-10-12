# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root: return res
        def helper(node,level):
            if len(res)==level: res.append([])
            res[level].append(node.val)
            if node.left: helper(node.left,level+1)
            if node.right: helper(node.right,level+1)
        helper(root,0)
        return res