# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        if not root: return 0

        def isexist(root):
            if not root: return 0
            left, right = isexist(root.left), isexist(root.right)
            self.res = max(self.res, right, left)
            return max(left, right) + 1

        isexist(root)
        return self.res + 1

