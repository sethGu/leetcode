# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        tmp = []
        if not root: return tmp

        def helper(node, lvl):
            if len(tmp) == lvl: tmp.append([])
            tmp[lvl].append(node.val)
            if node.left: helper(node.left, lvl + 1)
            if node.right: helper(node.right, lvl + 1)

        helper(root, 0)
        for i in range(len(tmp)):
            if i % 2 == 1: tmp[i] = tmp[i][::-1]

        return tmp