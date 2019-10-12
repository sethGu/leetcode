# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        def findmax(root):
            if not root: return 0
            left, right = findmax(root.left), findmax(root.right)
            return max(left, right) + 1

        return abs(findmax(root.left)-findmax(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)