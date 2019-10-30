# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return
        node=TreeNode(preorder[0])
        node_index=inorder.index(node.val)
        # inorder中左子树多多少个，其中的node_index就会往后多少个
        # 因此preorder中的左子树区间就会向后多少个
        # 即node的左子树个数就是node_index
        node.left=self.buildTree(preorder[1:node_index+1],inorder[0:node_index])
        node.right=self.buildTree(preorder[node_index+1:],inorder[node_index+1:])
        return node