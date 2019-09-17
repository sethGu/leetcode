# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        def isexist(root):
            if not root: return 0
            left,right=isexist(root.left),isexist(root.right)
            self.res=max(self.res,left+right)
            return max(left,right)+1
        isexist(root)
        return self.res






# 强行遍历无法通过所有测试用例，遗憾失败
# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         self.l,self.r=0,0
#         # 遍历左
#         def isexist_l(root):
#             if not root: return 0
#             if root.left:
#                 self.l+=1
#                 if not root.left.left:
#                     if root.left.right: isexist_r(root.left)
#                 else: isexist_l(root.left)
#             return self.l
#         #遍历右
#         def isexist_r(root):
#             if not root: return 0
#             if root.right:
#                 self.r+=1
#                 if not root.right.right:
#                     if root.right.left: isexist_l(root.right)
#                 else: isexist_r(root.right)
#             return self.r
#         isexist_l(root)
#         isexist_r(root)
#         return self.l+self.r